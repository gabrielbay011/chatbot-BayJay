from models.processer import Processer
from models.extractor import Extractor
import os
from models.aibay import AIBay
from utils import content
from models.message import Message

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
                    a = AIBay(content)
                    while True:
                        pergunta = input("Faça a pergunta")
                        m = Message(pergunta)
                        a.make_message(m)
                        print(m.response)
        else:
            print("Vazio")