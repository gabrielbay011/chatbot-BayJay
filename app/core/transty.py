from AI import AI


class Transty:

    def __init__(self, model:AI):
        self._model = model

    def to_comunicate(self, msg):
        self._model.send_message(msg)
