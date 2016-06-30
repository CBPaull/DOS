from system.core.router import routes

# Default Welcome Page.  Render
routes['default_controller'] = 'Users'
# Login Registration Page. Render
routes['/users/logreg'] = 'Users#index'
# Show all users. Render
routes['/users/showall'] =  'Users#showall'
# Show User page. Render
routes['/users/show/<user_id>'] = 'Users#show'
# Edit User page. Render
routes['/users/edit/<user_id>'] = 'Users#edit'
# Show Vendor page. Render
routes['/users/vendor/<user_id>'] = 'Users#vendor'
# Show Contractor page. Render
routes['/users/contractor/<user_id>'] = 'Users#contractor'
# Show search page. Render
routes['/search'] = 'Users#search'
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
# Process update job address.
routes['POST']['/jobs/update_address/<job_id>'] = 'Jobs#update_address'
# Process job status. (Change job status)
routes['POST']['/jobs/update_status/<job_id>'] = 'Jobs#confirm'
# Process Destroy user
routes['POST']['/users/destroy/<user_id>'] = 'Users#destroy'
#Process Destroy address
routes['POST']['/users/destroyaddress/<address_id>'] = 'Users#destroyaddress'
# Process destroy job
routes['POST']['/jobs/destroy/<job_id>'] = 'Jobs#destroy'
# process make bid
routes['POST']['/jobs/makebid'] = 'Jobs#makebid'
#process change bid status
routes['POST']['/jobs/changebidstatus'] = 'Jobs#changebidstatus'
# destroy bid
routes['POST']['/jobs/removebid'] = 'Jobs#removebid'

#Job reviews
routes['/jobs/add_review/<job_id>'] = 'Jobs#add_review'
routes['/jobs/add_review_c/<job_id>'] = 'Jobs#add_review_c'

#Process Job Review
routes['POST']['/jobs/create_review'] = 'Jobs#create_review'

# add routes to create, edit, view, and destroy contractor reviews
# Show all bids on job_id.  Render
# routes['/bids/<job_id>'] 'Bids#show'
# routes['POST']['/bids/add/<job_id>'] = 'Bids#add'
# routes['POST']['/bids/counter/<bid_id>'] = 'Bids#counter'
# routes['POST']['/bids/accept/<bid_id>'] = 'Bids#accept'