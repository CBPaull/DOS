from system.core.controller import *


class Jobs(Controller):
    def __init__(self, action):
        super(Jobs, self).__init__(action)
        self.load_model('Job')
        self.load.model('User')
        self.db = self._app.db

    def index(self):

        return self.load_view('index.html')

