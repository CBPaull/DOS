from system.core.router import routes

# Default Welcome Page.  Render
routes['default_controller'] = 'Users'
# Login Registration Page. Render
routes['/users/logreg'] = 'Users#logreg'
# Show User page. Render
routes['/users/show/<user_id>'] 'Users#show'
# Edit User page. Render
routes['/users/edit/<user_id>'] 'Users#edit'
# Show Vendor page. Render
routes['/users/vendor/<user_id>'] = 'Users#vendor'
# Show Contractor page. Render
routes['/users/contractor'] = 'Users#contractor'
# Show search page. Render
routes['/search'] = 'Users#search'
# List of all users. Render
routes['/users/userlist'] 'Users#userlist'
# Page for adding new job. Render.
routes['/jobs/addnew'] = 'Jobs#addnew'
# Show wall of jobs. Render
routes['/jobs/joblist'] = 'Jobs#joblist'
# Show job by job_id
routes['/jobs/show/<job_id>'] = 'Jobs#show'
# Edit job by job_id
routes['/jobs/edit/<job_id>'] = 'Jobs#edit'
# Process create user.
routes['POST']['/users/create']='Users#create'
# Process Login user.
routes['POST']['/users/login']='Users#login'
# Process logout user.
routes['POST']['/users/logout']='Users#logout'
# Process Update user.
routes['POST']['/users/update/<user_id>'] = 'Users#update'
# Process Update user address
routes['POST']['/users/update_address/<user_id>'] = 'Users#update_address'
# Process Create Job.
routes['POST']['/jobs/add'] = 'Jobs#add'
# Process update job.
routes['POST']['/jobs/update/<job_id>'] = 'Jobs#update'
# Process job status. (Change job status)
routes['POST']['/jobs/update_status/<job_id>'] = 'Jobs#confirm'
# Process Destroy user
routes['POST']['/users/destroy/<user_id'] = 'Users#destroy'
# Process destroy job
routes['POST']['/jobs/destroy/<job_id>']


# Show all bids on job_id.  Render
# routes['/bids/<job_id>'] 'Bids#show'
# routes['POST']['/bids/add/<job_id>'] = 'Bids#add'
# routes['POST']['/bids/counter/<bid_id>'] = 'Bids#counter'
# routes['POST']['/bids/accept/<bid_id>'] = 'Bids#accept'