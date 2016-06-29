from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('Job')
        self.load_model('User')
        self.db = self._app.db

    def index(self):
        return self.load_view('/users/login_registration.html')

    def logreg(self):
        return self.load_view('/users/login_registration.html')

    def showall(self):
        all_users = self.models['User'].get_all_users()
        return self.load_view('allusers.html', all_users=all_users)

    # user list
    def vendor(self, u_id):
        user = self.models['User'].show_user(u_id)
        vendor = self.models['User'].show_vendor(u_id)
        address = self.models['User'].show_addresses
        jobs = self.models['Job'].get_jobs_by_userid(u_id)
        return self.load_view('/users/dashboard_employer.html', user= user, address= address, jobs= jobs)

    def contractor(self, u_id):
        # This will differentiate from vendor dashboard when we add contractors
        user = self.models['User'].show_user(u_id)
        address = self.models['User'].show_addresses
        jobs = self.models['Job'].get_jobs_by_userid(u_id)
        return self.load_view('/users/dashboard_employer.html', user=user, address=address, jobs=jobs)

    def show(self, u_id):
        user = self.models['User'].show_user(u_id)
        return self.load_view('/users/show_user.html', user= user)

    def edit(self):
        u_id = session['id']
        user = self.models['User'].show_user(u_id)
        return self.load_view('users/edit_user', user= user)

    def login(self):
        requestform = request.form
        user = self.models['User'].login_user(requestform)
        session['id'] = user['id']
        return redirect('/users/show_employer_dashboard')


    def create(self):
        requestform = request.form
        user = self.models['User'].add_user(requestform)
        print user
        session['id'] = user['id']
        return redirect('/users/show_employer_dashboard')

    def update(self, u_id):
        user = self.models['User'].update_user(requestform)
        session['id'] = user['id']
        return redirect('/users/show_employer_dashboard')
        # POST pass requestform to model update

    def update_address(self, u_id):
        requestform = request.form
        user = self.models['User'].insert_address(requestform, u_id)
        session['id'] = user['id']
        return redirect('/users/show_employer_dashboard')
        #Insert new address, addresses can be added or deleted.
        # #Delete removes foreign key assignment

    def destroy(self):
        requestform = request.form
        self.models['User'].delete_user(requestform)
        return redirect('users/show_users')

    def destroyaddress(self):
        requestform = request.form
        self.models['User'].delete_address(requestform)
        return redirect('/users/show_employer_dashboard')


