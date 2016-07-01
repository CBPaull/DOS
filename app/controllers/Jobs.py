from system.core.controller import *

class Jobs(Controller):
    def __init__(self, action):
        super(Jobs, self).__init__(action)
        self.load_model('Job')
        self.load_model('User')
        self.load_model('Bid')
        self.load_model('Review')
        self.db = self._app.db

    def joblist(self):
        # ['/jobs/joblist']
        # Show wall of jobs. Render
        all_jobs = self.models['Job'].get_all_jobs()
        print all_jobs
        return self.load_view('jobs/joblist.html', all_jobs=all_jobs)

    def addnew(self):
        # Page for adding new job. Render.
        return self.load_view('jobs/addnew.html')

    def show(self, job_id):
        # Show job by job_id. Render
        job = self.models['Job'].get_job_by_id(job_id)

        if len(job[0]['apartment']) != 0:
            address = str(job[0]['address1']) + ' ' + str(job[0]['apartment']) + ' '  + str(job[0]['city']) + ' '  + str(job[0]['zipcode'])
        else:
            address = str(job[0]['address1']) + ' '  + str(job[0]['city']) + ' '  + str(job[0]['zipcode'])
        
        latlong = self.models['Job'].job_location_latitude_longtitude(address)
        bids = self.models['Bid'].show_job_bids(job_id)
        return self.load_view('/jobs/show.html', job=job[0], latlong=latlong, bids=bids)

    def edit(self, job_id):
        # Edit job by job_id. Render
        job = self.models['Job'].get_job_by_id(job_id)
        return self.load_view('jobs/edit.html', job=job[0])

    def add(self):
        # Process create job. Redirect
        input_form = request.form
        create_status = self.models['Job'].create_job(input_form)
        if create_status['status']:
            return redirect('/jobs/show/' + str(create_status['job_id']))
        else:
            return redirect('jobs/addnew')

    def update(self, job_id):
        # Process update job. Redirect
        input_form = request.form
        update_status = self.models['Job'].update_job(input_form, job_id)
        if update_status['status']:
            return redirect('/jobs/show/' + str(update_status['job_id']))
        else:
            return redirect('/jobs/edit/' + str(update_status['job_id']))

    def update_address(self, job_id):
        # Process update job. Redirect
        input_form = request.form
        update_status = self.models['Job'].update_job_address(input_form, job_id)
        if update_status['status']:
            return redirect('/jobs/show/' + str(update_status['job_id']))
        else:
            return redirect('/jobs/edit/' + str(update_status['job_id']))

    def confirm(self, job_id):
        # Process job status to 'completed'. Redirect
        self.models['Job'].job_change_status(job_id, 2)
        # sending email out to job posters and contractors
        # users = self.models['Job'].get_users_from_job(job_id)
        # job = self.models['Job'].get_job_by_id(job_id)
        # self.models['Email'].send_review_emails(users, job)
        return redirect('/jobs/show/' + str(job_id))

    def destroy(self, job_id):
        # Process destroy job. Redirect
        self.models['Job'].destroy_job(job_id)
        return redirect('/jobs/joblist')

    def makebid(self):
        requestform = request.form
        print requestform
        create_status = self.models['Bid'].create_bid(requestform)
        if create_status['status']:
            return redirect('/jobs/show/' + str(create_status['job_id']))
        else:
            return redirect('/jobs/show/' + str(create_status['job_id']))

    def changebidstatus(self):
        # bid status in request form will either be a 1 for rejecting a bid
        # or  a 2 for accepting a bid.
        # other things like id, user_id, and job_id will be stored in 
        # hidden values as well.
        requestform = request.form
        change_status = self.models['Bid'].change_bid_status(requestform)
        if change_status['status']:
            return redirect('/jobs/show/' + str(change_status['job_id']))
        else:
            return redirect('/jobs/show/' + str(change_status['job_id']))

    def removebid(self):
        requestform = request.form
        remove_status = self.models['Bid'].destroy_bid(requestform)
        if remove_status['status']:
            return redirect('/jobs/show/' + str(remove_status['job_id']))
        else:
            return redirect('/jobs/show/' + str(create_status['job_id']))

    def add_review(self, job_id):
        # Displays a job review page.  Render.
        #
        job = self.models['Job'].get_job_by_id(job_id)
        print job[0]
        return self.load_view('/jobs/addreview.html', job=job[0])

    def add_review_c(self, job_id):
        # Displays a job review page.  Render.
        job = self.models['Job'].get_job_by_id(job_id)
        print job[0]
        return self.load_view('/jobs/addreview_c.html', job=job[0])

    def create_review(self):
        input_form = request.form
        print "input form review", input_form
        review_status = self.models['Review'].create_review(input_form)
        return redirect('/users/show/'+str(session['id']))