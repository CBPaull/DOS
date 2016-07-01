from system.core.controller import *

class Web(Controller):
    def __init__(self, action):
        super(Web, self).__init__(action)
        self.db = self._app.db

    def about(self):
        return self.load_view('about.html')

    def contact(self):
        return self.load_view('contact.html')

