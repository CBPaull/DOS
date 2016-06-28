from system.core.controller import *


class Jobs(Controller):
    def __init__(self, action):
        super(Jobs, self).__init__(action)
        self.load_model('Job')
        self.load.model('User')
        self.db = self._app.db

    def index(self):
    	# Adding more stuff here.
        return self.load_view('index.html')

    def show_all_job(self):
    	all_jobs = self.model['Job'].get_all_jobs()
    	return self.load_view('jobs.html', all_jobs=all_jobs)