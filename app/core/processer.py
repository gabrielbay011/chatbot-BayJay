import subprocess
import os
import shutil

class Installer:

    def __init__(self):
        self._repo = None
        self._local = "repositorio_temporario"
        self.__ssh = None #todo: SSH para auntenticação

    def make_clone(self, repo: str):
        """This method return a new local repository"""
        self._repo = repo
        #if self._check_url(self._repo):
        try:
                result = subprocess.run(
                    ["git", "clone", self._repo, self._local],
                    capture_output=True,
                    text=True,
                    check=True
                )
                print("Clonagem concluida")
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

        #else:
            #return "INVALID"

    def delete_repository(self):
        try:
            if os.path.exists(self._local):
                shutil.rmtree(self._local)
                print(f"Repositório '{self._local}' apagado com sucesso.")
            else:
                print(f"Diretório '{self._local}' não encontrado para apagar.")
        except OSError as e:
            print(f"Erro ao apagar o diretório '{self._local}': {e}")

    def _check_url(self, value):
        if "https://github.com/baymetrics/" in value: return True
        return False

    def get_local_path(self):
        """Retorna o caminho local onde o repositório foi clonado."""
        return self._local
