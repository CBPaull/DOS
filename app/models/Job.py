from system.core.model import Model

JOB_STATUS = ['open', 'closed', 'completed', 'failed']

class Job(Model):

    def __init__(self):
        super(Job, self).__init__()

    def get_all_jobs(self):
        query = "SELECT jobs.id AS 'job_id', jobs.title AS 'job_title', jobs.description AS 'job_description', " \
                "user_id, jobs.time AS 'job_time', jobs.created_at AS 'posted_at', users.firstname AS 'firstname', "\
                "users.lastname AS 'lastname', users.email AS 'email', users.phone AS 'phone', addresses.address1, " \
                "addresses.apartment, addresses.city, addresses.zipcode  FROM jobs " \
                "JOIN users ON jobs.user_id = users.id  JOIN jobs_has_addresses ON jobs.id = jobs_has_addresses.jobs_id" \
                " JOIN addresses ON jobs_has_addresses.addresses_id = addresses.id; "
        all_jobs = self.db.query_db(query)
        return all_jobs

    def get_job_by_id(self, job_id):
        data = {
            'job_id': job_id
        }
        query = "SELECT jobs.id AS 'job_id', jobs.title AS 'job_title', jobs.description AS 'job_description', " \
                "user_id, jobs.time AS 'job_time', jobs.created_at AS 'posted_at', users.firstname AS 'firstname', "\
                "users.lastname AS 'lastname', users.email AS 'email', users.phone AS 'phone', addresses.address1, " \
                "addresses.apartment, addresses.city, addresses.zipcode, jobs.status  FROM jobs " \
                "JOIN users ON jobs.user_id = users.id  JOIN jobs_has_addresses ON jobs.id = jobs_has_addresses.jobs_id" \
                " JOIN addresses ON jobs_has_addresses.addresses_id = addresses.id " \
                "WHERE jobs.id = :job_id; "
        job = self.db.query_db(query, data)
        return job

    def get_jobs_by_userid(self, user_id):
        data = {
            'user_id': user_id
        }
        query = "SELECT jobs.id AS 'job_id', jobs.title AS 'job_title', jobs.description AS 'job_description', " \
                "user_id, jobs.time AS 'job_time', jobs.created_at AS 'posted_at', users.firstname AS 'firstname', " \
                "users.lastname AS 'lastname', users.email AS 'email', users.phone AS 'phone', addresses.address1, " \
                "addresses.apartment, addresses.city, addresses.zipcode, jobs.status   FROM jobs " \
                "JOIN users ON jobs.user_id = users.id  JOIN jobs_has_addresses ON jobs.id = jobs_has_addresses.jobs_id" \
                " JOIN addresses ON jobs_has_addresses.addresses_id = addresses.id " \
                "WHERE user.id = :user_id; "
        jobs = self.db.query_db(query, data)
        return jobs

    def create_job(self, input_form):
        # ToDo - add skills
        #
        # Data structuring
        data = {
            'title': input_form['title'],
            'description': input_form['description'],
            'user_id': input_form['user_id'],
            'time': input_form['time'],
            'status': JOB_STATUS[0],
        }
        query = "INSERT INTO jobs(title, description, user_id, time, status, created_at, updated_at) " \
                "VALUES (:title, :description, :user_id, :time, : status, NOW(), NOW())"
        job_id = self.db.query_db(query, data)
        data2 = {
            'apartment': input_form['apartment'],
            'address1': input_form['address'],
            'city': input_form['city'],
            'zipcode': input_form['zipcode']
        }
        query2 = "INSERT INTO addresses(apartment, address, city, zipcode) " \
                 "VALUES(:apartment, :address1, :city, :zipcode);"
        address_id = self.db.query_db(query2, data2)
        data3 = {
            'job_id': job_id,
            'address_id': address_id
        }
        query3 = "INSERT INTO jobs_has_addresses(job_id, address_id) VALUES(:job_id, :address_id);"
        self.db.query_db(query3, data3)
        return {'status': True, 'job_id': job_id}

    def job_change_status(self, job_id, job_stat):
        # Change job status ['open, 'closed', 'completed', 'failed']
        data = {
            'job_id': job_id,
            'status': JOB_STATUS[job_stat]
        }
        query = "UPDATE jobs SET status = :status WHERE id=:job_id;"
        self.db.query_db(query, data)
        return


    def destroy_jobs(self, job_id):
        # Destory a job.  Delete from database.  *Uses cascade delete
        data = {
            'job_id': job_id
        }
        query = "DELETE FROM jobs WHERE id=:job_id"
        self.db.query_db(query, data)
        return

