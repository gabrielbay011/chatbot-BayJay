import subprocess
import os
import shutil

class Processer:

    def __init__(self, repo: str):
        self._repo = repo
        self._local = "Repositorio temporário"

    def make_clone(self):
        """This method return a new local repository"""
        try:
            result = subprocess.run(
                ["git", "clone", self._repo, self._local],
                capture_output=True,
                text=True,
                check=True
            )
            return result
        except subprocess.CalledProcessError as e:
            print(f"Erro ao clonar o repositório: {e}")
            print("Stdout:", e.stdout)
            print("Stderr:", e.stderr)
            print("Abortando...")
            return
        except FileNotFoundError:
            print("Erro: 'git' não encontrado. Certifique-se de que o Git está instalado e no PATH.")
            print("Abortando...")
            return

    def delete_repository(self):
        try:
            if os.path.exists(self._local):
                shutil.rmtree(self._local)
                print(f"Repositório '{self._local}' apagado com sucesso.")
            else:
                print(f"Diretório '{self._local}' não encontrado para apagar.")
        except OSError as e:
            print(f"Erro ao apagar o diretório '{self._local}': {e}")

    def get_local_path(self):
        """Retorna o caminho local onde o repositório foi clonado."""
        return self._local

class Extractor:

    def __init__(self):
        self._extracted_content = {}
        self.ignore_file_extensions = (
            '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.ico', # Imagens
            '.zip', '.tar', '.gz', '.rar', '.7z', # Arquivos comprimidos
            '.exe', '.dll', '.bin', '.obj', '.so', '.lib', # Binários executáveis/bibliotecas
            '.pdf', '.docx', '.xlsx', '.pptx', # Documentos complexos (requerem parsers específicos)
            '.log', '.sqlite', '.db', # Logs e bancos de dados
            '.DS_Store', 'Thumbs.db', # Arquivos de sistema
            '.lock', '.swp' # Arquivos de bloqueio/temporários
        )
        self.ignored_folder_names = (
            '.git', '.vscode', '__pycache__', 'node_modules',
            'venv', '.venv', 'env', '.env', 'build', 'dist',
            'target', 'out', 'bin'
        )

    def _should_ignore_file(self, file_path):
        """Verifica se um arquivo deve ser ignorado com base em sua extensão e caminho."""
        # Ignorar por extensão
        if file_path.lower().endswith(self.ignore_file_extensions):
            return True

        # Ignorar por nome/caminho da pasta
        for folder_name in self.ignored_folder_names:
            # Verifica se o nome da pasta ignorada está no caminho completo
            if f"/{folder_name}/" in file_path.replace("\\", "/"):  # Normaliza barras para consistência
                return True
            # Adicionalmente, verifica se a pasta começa com o nome ignorado para a própria pasta raiz (ex: .git no root)
            if file_path.replace("\\", "/").startswith(f"{folder_name}/"):
                return True
        return False

    def _read_local_file_content(self, file_path):
        """
        Método responsável por ler o conteúdo de um arquivo local.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            print(f"Aviso: Não foi possível decodificar '{file_path}' como UTF-8. Pulando.")
            return None
        except Exception as e:
            print(f"Erro ao ler '{file_path}': {e}")
            return None

    def extract_from_local_folder(self, root_folder_path):
        """
        Método principal para extrair o conteúdo dos arquivos de uma pasta local.
        Este método agora é o principal ponto de entrada para a extração,
        assumindo que o repositório já foi clonado.

        Args:
            root_folder_path (str): O caminho completo para a pasta (o repositório clonado)
                                      que contém os arquivos a serem extraídos.
        """
        self.extracted_content = {}  # Limpa o conteúdo anterior

        if not os.path.isdir(root_folder_path):
            print(f"Erro: A pasta '{root_folder_path}' não foi encontrada ou não é um diretório válido.")
            return

        print(f"Iniciando extração de arquivos em: {root_folder_path}")

        # A chave de nível superior para o dicionário será o caminho da pasta raiz fornecida
        self.extracted_content[root_folder_path] = {}

        for root, _, files in os.walk(root_folder_path):
            for file_name in files:
                full_file_path = os.path.join(root, file_name)

                # Ignorar arquivos em pastas ignoradas ou com extensões ignoradas
                if self._should_ignore_file(os.path.relpath(full_file_path, root_folder_path)):
                    print(f"Pulando arquivo ignorado: {full_file_path}")
                    continue

                relative_path = os.path.relpath(full_file_path, root_folder_path)
                content = self._read_local_file_content(full_file_path)
                if content is not None:
                    self.extracted_content[root_folder_path][relative_path] = content
                    # print(f"Extraído: {relative_path}") # Descomente para ver cada arquivo sendo extraído

        print(
            f"Extração local concluída para '{root_folder_path}'. Total de arquivos: {len(self.extracted_content[root_folder_path])}")

    def get_extracted_content(self):
        """
        Retorna o dicionário com todo o conteúdo extraído.
        """
        return self.extracted_content

# --- Exemplo de Uso Integrado ---
if __name__ == "__main__":

    # URL de um repositório GitHub público para teste
    github_repo_url = "https://github.com/gabrielbay011/SysFlow-.git"  # Exemplo público

    # 1. Instanciar e usar a classe Processer para clonar
    processor = Processer(github_repo_url)

    # Se o diretório temporário já existe (de uma execução anterior), apague-o primeiro
    if os.path.exists(processor.get_local_path()):
        processor.delete_repository()

    clone_successful = processor.make_clone()

    if clone_successful:
        local_repo_path = processor.get_local_path()
        print(f"\nRepositório clonado para: {local_repo_path}")

        # 2. Instanciar e usar a classe CodeExtractor para extrair o conteúdo do repositório clonado
        code_extractor = Extractor()
        code_extractor.extract_from_local_folder(local_repo_path)

        extracted_data = code_extractor.get_extracted_content()

        print("\n--- Conteúdo Extraído do Repositório Clonado (Estrutura Resumida) ---")

        if extracted_data:
            for repo_root_path, files_data in extracted_data.items():
                print(f"Repositório Local: {repo_root_path}")
                # Mostra apenas os primeiros 5 arquivos para não poluir muito a saída
                count = 0
                for file_rel_path, content in files_data.items():
                    if count < 5:
                        print(f"  - {file_rel_path}: {content}...")
                        count += 1
                    else:
                        break
                if len(files_data) > 5:
                    print(f"  ... e mais {len(files_data) - 5} arquivos.")
        else:
            print("Nenhum conteúdo extraído do repositório clonado.")

        # 3. Limpar: Apagar o repositório local após a extração
        processor.delete_repository()
    else:
        print("Não foi possível continuar sem um repositório clonado com sucesso.")
