from app.core.message import Message
from app.core.transty import Transty
from app.core.AI import AIGemini



class People:

    def __init__(self, name:str, email:str, password = None | str, id = None | int):
        self._name = name
        self._email = email
        self._password = password
        self._id = id

class User(People):

    def __init__(self, name:str, email:str, session:str, password = None | str, id = None | str):
        super().__init__(name, email , password, id)
        self._session = session

    def to_ask(self, content_msg):
        msg = Message(content_msg)
        if isinstance(content_msg, str):
            transtynne.to_comunicate(msg)
        return print(msg.response)

if __name__ == "__main__":
    victor = User("Victor", "@seillaoque", "qualquercoisa"," 122525")


    gemini = AIGemini("")
    transtynne = Transty(gemini)

    victor.to_ask("Olá tudo bem, se apresente")