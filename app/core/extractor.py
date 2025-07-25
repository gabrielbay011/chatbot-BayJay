import os
from app.core.processer import Processer

class Extractor:

    def __init__(self):
        self._extracted_content = {}
        self.ignore_file_extensions = (
            '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.ico',  # Imagens
            '.zip', '.tar', '.gz', '.rar', '.7z',  # Arquivos comprimidos
            '.exe', '.dll', '.bin', '.obj', '.so', '.lib',  # Binários executáveis/bibliotecas
            '.pdf', '.docx', '.xlsx', '.pptx',  # Documentos complexos (requerem parsers específicos)
            '.log', '.sqlite', '.db',  # Logs e bancos de dados
            '.DS_Store', 'Thumbs.db',  # Arquivos de sistema
            '.lock', '.swp'  # Arquivos de bloqueio/temporários
        )
        self.ignored_folder_names = (
            '.git', '.vscode', '__pycache__', 'node_modules',
            'venv', '.venv', 'env', '.env', 'build', 'dist',
            'target', 'out', 'bin'
        )

    def _ignore_file(self, file_path: str):
        if file_path.lower().endswith(self.ignore_file_extensions): return True

        for folder_name in self.ignored_folder_names:
            if f"/{folder_name}/" in file_path.replace("\\", "/"): return True
            if file_path.replace("\\", "/").startswith(f"/{folder_name}/"): return True
        return False

    def read_file(self, file_path: str):
        try:
            with open(file_path, 'r', encoding='utf-8') as f: return f.read()
        except UnicodeDecodeError:
            print(f"Aviso: Não foi possível decodificar '{file_path}' como UTF-8. Pulando.")
            return None
        except Exception as e:
            print(f"Erro ao ler '{file_path}': {e}")
            return None

    def extract_from_local_folder(self, root_folder_path):
        self._extracted_content = {}

        if not os.path.isdir(root_folder_path):
            print(f"Erro: A pasta '{root_folder_path}' não foi encontrada ou não é um diretório válido.")
            return

        self._extracted_content[root_folder_path] = {}

        for root, _, files in os.walk(root_folder_path):
            for file_name in files:
                full_file_path = os.path.join(root, file_name)

                if self._ignore_file(os.path.relpath(full_file_path, root_folder_path)):
                    print(f"Pulando arquivo ignorado: {full_file_path}")
                    continue

                relative_path = os.path.relpath(full_file_path, root_folder_path)
                content = self.read_file(full_file_path)
                if content is not None:
                    self._extracted_content[root_folder_path][relative_path] = content

    def get_extracted_content(self):
        return self._extracted_content

if __name__ == "__main__":
    repo = "https://github.com/gabrielbay011/SysFlow-.git"
    p = Processer(repo)

    if os.path.exists(p.get_local_path()):
        p.delete_repository()
    clone_successful = p.make_clone()

    if clone_successful:
        local_repo_path = p.get_local_path()

        e = Extractor()
        e.extract_from_local_folder(local_repo_path)

        extracted_data = e.get_extracted_content()
        if extracted_data:
            for repo_root_path, files_data in extracted_data.items():
                for content in files_data.items():
                    print(content)

        else:
            print("Vazio")
