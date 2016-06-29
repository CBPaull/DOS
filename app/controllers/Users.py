from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

    def index(self):
        return self.load_view('/users/login_registration.html')

    def show_users(self):
        all_users = self.model['User'].get_all_users()
        return self.load_view('allusers.html', all_users=all_users)

    # user list
    def show_employer_dashboard(self):
        u_id = session['id']
        user = self.model['User'].show_user(u_id)
        vendor = self.model['User'].show_vendor(u_id)
        address = self.model['User'].show_addresses
        jobs = self.model['Job'].get_jobs_by_userid(u_id)
        return self.load_view('/users/dashboard_employer.html', user= user, address= address, jobs= jobs)

    def show_employee_dashboard(self):
        # This will differentiate from vendor dashboard when we add contractors
        u_id = session['id']
        user = self.model['User'].show_user(u_id)
        address = self.model['User'].show_addresses
        jobs = self.model['Job'].get_jobs_by_userid(u_id)
        return self.load_view('/users/dashboard_employer.html', user=user, address=address, jobs=jobs)

    def show_user(self, u_id):
        user = self.model['User'].show_user(u_id)
        return self.load_view('/users/show_user.html', user= user)

    def edit_user(self):
        u_id = session['id']
        user = self.model['User'].show_user(u_id)
        return self.load_view('users/edit_user', user= user)

    def userlogin(self):
        requestform = request.form
        user = self.model['User'].login_user(requestform)
        session['id'] = user['id']
        return redirect('/users/show_employer_dashboard')


    def useradd(self):
        requestform = request.form
        user = self.model['User'].add_user(requestform)
        session['id'] = user['id']
        return redirect('/users/show_employer_dashboard')

    def userupdate(self):
        requestform = request.form
        user = self.model['User'].update_user(requestform)
        session['id'] = user['id']
        return redirect('/users/show_employer_dashboard')
        # POST pass requestform to model update

    def addaddress(self):
        u_id = session['id']
        requestform = request.form
        user = self.model['User'].insert_address(requestform, u_id)
        session['id'] = user['id']
        return redirect('/users/show_employer_dashboard')
        #Insert new address, addresses can be added or deleted.
        # #Delete removes foreign key assignment

    def removeuser(self):
        requestform = request.form
        self.model['User'].delete_user(requestform)
        return redirect('users/show_users')

    def removeaddress(self):
        requestform = request.form
        self.model['User'].delete_address(requestform)
        return redirect('/users/show_employer_dashboard')


