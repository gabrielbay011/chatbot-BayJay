from dotenv import load_dotenv
from google import genai
from google.genai import types

from app.core.message import Message

load_dotenv()

client = genai.Client()
class AIBay:

    def __init__(self, content):
        self._model = "gemini-2.5-flash"
        self._client = genai.Client()
        self._content = content


    def make_message(self, msg: Message):
        msg.response = client.models.generate_content(
            model=self._model,
            config=types.GenerateContentConfig(
                system_instruction = self._content,
            ),
            contents = msg.content
        ).text


