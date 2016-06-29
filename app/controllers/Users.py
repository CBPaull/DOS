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
        # print all_users
        return self.load_view('users/allusers.html', all_users=all_users)

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

    def show(self, user_id):
        user = self.models['User'].show_user(user_id)
        print user
        return self.load_view('/users/show.html', user=user[0])

    def edit(self):
        u_id = session['id']
        user = self.models['User'].show_user(u_id)
        return self.load_view('users/edit.html', user= user)

    def login(self):
        requestform = request.form
        login_status = self.models['User'].login_user(requestform)
        if login_status['status']:
            session['id'] = login_status['user']['id']
            return redirect('/users/show/'+str(session['id']))
        else:
            for error in login_status['errors']:
                flash(error)
            return redirect('/')


    def create(self):
        requestform = request.form
        create_status = self.models['User'].add_user(requestform)
        print create_status
        if create_status['status']:
            session['id'] = create_status['user']['id']
            return redirect('/users/show/'+str(session['id']))
        else:
            for error in create_status['errors']:
                flash(error)
            return redirect('/')

    def update(self, u_id):
        update_status = self.models['User'].update_user(requestform)
        return redirect('/users/vendor/'+str(session['id']))
        # POST pass requestform to model update

    def update_address(self, u_id):
        requestform = request.form
        update_status = self.models['User'].insert_address(requestform, u_id)
        session['id'] = update_status['user']['id']
        return redirect('/users/vendor/'+str(session['id']))
        #Insert new address, addresses can be added or deleted.
        # #Delete removes foreign key assignment

    def destroy(self):
        requestform = request.form
        self.models['User'].delete_user(requestform)
        return redirect('users/show_users')

    def destroyaddress(self):
        requestform = request.form
        self.models['User'].delete_address(requestform)
        return redirect('/users/vendor/'+str(session['id']))


