from abc import ABC, abstractmethod
from google.genai import types
from google import genai
from dotenv import load_dotenv
from recipient import Recipient
from app.utils import INSTRUCTIONS
from message import  Message
from app.core.extractor import Extractor
from app.core.processer import Installer

load_dotenv()

class AI(ABC):
    """
    This is an Interface what implements all functions of Artificial Inteligente
    """
    @abstractmethod
    def send_message(self, msg): pass

class AIChatGpt(AI):
    def __init__(self): pass
    def send_message(self):pass

class AIGemini(AI):
    def __init__(self, content: Recipient):
        self._model = "gemini-2.5-pro"
        self._client = genai.Client()
        #self._content = content.get_context()
        #self._client.models.generate_content(model=self._model, config=types.GenerateContentConfig(system_instruction=INSTRUCTIONS), contents=)

    def send_message(self, msg:Message):
        msg.response = self._client.models.generate_content(
            model=self._model,
            config=types.GenerateContentConfig(system_instruction=INSTRUCTIONS),
            contents= msg.content
        ).text

class AIDeepseeak(AI):
    def send_message(self): pass


if __name__ == "__main__":
    # REPOSITORIO DE TESTE E MENSAGENS
    repositorio = "https://github.com/gabrielbay011/SysFlow-"

    pergunta1 = "\033[32m  1 - Quem criou você ? \033[0m \n"
    pergunta2 = "\033[32m  2 - Baseado nesse repositório, quais roles existem no Banco de Dados ? \033[0m \n"
    pergunta3 = "\033[32m  3 - Elabore uma explicação sobre os riscos de segurança que existem nesse texto? \033[0m \n"
    pergunta4 = "\033[32m  4 - O que está no readme resumidamente nesse texto que te passei? \033[0m \n"
    pergunta5 = "\033[32m  5 - Dê dicas de Melhorias dessa documentação  \033[0m \n"
    pergunta6 = "\033[32m  6 - Passe o código dos grants que está na documentação?  \033[0m \n"
    pergunta7 = "\033[32m  7 - Que dia é Hoje ? \033[0m \n"

    # CRIANDO OS OBJETOS...
    gemini = AIGemini("g")
    chatgpt = AIChatGpt()
    deepseeak = AIDeepseeak()
    extractor = Extractor()
    installer_repo = Installer()

    # BAIXAR REPOSITORIO NA MÁQUINA
    installer_repo.make_clone(repositorio)

    # EXTRAIR ARQUIVOS
    extractor.extract_from_local_folder(installer_repo.get_local_path())

    # MENSSAGEM SENDO CRIADA
    print("==============================================================================================================")

    msg1 = Message(pergunta1)
    msg2 = Message(f"{extractor.get_extracted_content()} {pergunta2}")
    msg3 = Message(f"{extractor.get_extracted_content()} {pergunta3}")
    msg4 = Message(f"{extractor.get_extracted_content()} {pergunta4}")
    msg5 = Message(f"{extractor.get_extracted_content()} {pergunta5}")
    msg6 = Message(f"{extractor.get_extracted_content()} {pergunta6}")
    msg7 = Message(f" {pergunta7}")

    print("==============================================================================================================")

    print(pergunta1)
    gemini.send_message(msg1) # A API RECEBE A MENSAGEM
    print( msg1.response)

    print("\n==============================================================================================================")

    print(pergunta2)
    gemini.send_message(msg2) # A API RECEBE A MENSAGEM
    print(msg2.response)

    print("\n==============================================================================================================")

    print(pergunta3)
    gemini.send_message(msg3) # A API RECEBE A MENSAGEM
    print(msg3.response)

    print("\n==============================================================================================================")

    print(pergunta4)
    gemini.send_message(msg4) # A API RECEBE A MENSAGEM
    print(msg4.response)

    print("\n==============================================================================================================")

    print(pergunta5)
    gemini.send_message(msg5) # A API RECEBE A MENSAGEM
    print(msg5.response)

    print("\n==============================================================================================================")

    print(pergunta6)
    gemini.send_message(msg6) # A API RECEBE A MENSAGEM
    print(msg6.response)

    print("\n==============================================================================================================")

    print(pergunta7)
    gemini.send_message(msg7) # A API RECEBE A MENSAGEM
    print( msg7.response)

    print("\n==============================================================================================================")



