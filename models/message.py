from datetime import datetime

class Message:

    def __init__(self, content):
        self._created_at = datetime.now()
        self._content = content
        self._response = None
        self._response_date = None

    @property
    def content(self):
        return self._content

    @property
    def response(self):
        return self.response

    @response.setter
    def response(self, response):
        self._response_date = datetime.now()
        self._response = response