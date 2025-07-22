from dotenv import load_dotenv
from google import genai
from google.genai import types

from message import Message
import dotenv
from utils import content

load_dotenv()

client = genai.Client()
class AIBay:

    def __init__(self):
        self._model = "gemini-2.5-flash"
        self._client = genai.Client()


    def make_message(self, msg: Message):
        response = client.models.generate_content(
            model=self._model,
            config=types.GenerateContentConfig(
                system_instruction = content,
            ),
            contents = msg.content
        )
        return response

if __name__ == "__main__":
    a = AIBay()
    m = Message("fale seu objetivo aqui ")
    texto = a.make_message(m)
    print(texto.text)