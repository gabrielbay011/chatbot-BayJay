from datetime import datetime

class Message:

    def __init__(self, content):
        self._created_at = datetime.now()
        self._content = content
        self._response = ""
        self._response_date = None

    @property
    def content(self):
        return self._content

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, new_response):
        self._response_date = datetime.now()
        self._response = new_response