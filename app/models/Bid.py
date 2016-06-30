from system.core.model import Model
import re
from twilio.rest import TwilioRestClient
# still need to import this module: we use regular expressions to validate email formats!

class Bid(Model):

	def show_job_bids(self, job_id):
		info = { 'job_id': job_id }
		query = "SELECT bids.id AS id, bids.price AS price, bids.comment AS comment, bids.status AS status, bids.created_at AS created_at, users.id AS user_id, users.firstname AS firstname, users.lastname AS lastname FROM jobs JOIN bids ON jobs.id = bids.job_id JOIN users ON bids.user_id = users.id WHERE jobs.id = :job_id ORDER BY bids.created_at DESC"
		bids = self.db.query_db(query, info)
		print "BIDS ARE HERE"
		print bids
		return bids

	def create_bid(self, requestform):
		print "BIDS START HERE"
		info = {
			'price': requestform['price'],
			'comment': requestform['comment'],
			'status': requestform['status'],
			'job_id': requestform['job_id'],
			'user_id': requestform['user_id']
		}
		print "BIDS START HERE"
		print info
		query = " INSERT INTO bids(price, comment, status, job_id, user_id, created_at, updated_at) VALUES(:price, :comment, :status, :job_id, :user_id, NOW(), NOW())"
		self.db.query_db(query, info)
		return {'status': True, 'job_id': requestform['job_id']}

	def change_bid_status(self, requestform):
		info = {
    		'id': requestform['id'],
    		'status': requestform['status'],
    		'user_id': requestform['user_id'],
    		'job_id': requestform['job_id']
    	}
		prevquery = "SELECT status, id FROM bids WHERE id = :id"
		prev_status = self.db.query_db(prevquery, info)
		query = "UPDATE bids SET status= :status, updated_at= NOW() WHERE id = :id"
		self.db.query_db(query, info)
		if info['status']== '2':
			rejectquery = "UPDATE bids SET status= 1, updated_at= NOW() WHERE job_id = :job_id AND id != :id"
			self.db.query_db(rejectquery, info)
			jobsquery = "UPDATE jobs SET status = 'closed', accepted_id = :user_id, updated_at = NOW() WHERE id= :job_id"
			self.db.query_db(jobsquery, info)
			employerinfo_query = "SELECT users.firstname, users.lastname, jobs.title from users join jobs on users.id = jobs.user_id join bids on jobs.id = bids.job_id WHERE jobs.id = :job_id"
			employerinfo = self.db.query_db(employerinfo_query, info)
			
			bider_query = "select users.phone from users join bids on bids.user_id = users.id WHERE bids.job_id = :job_id;"
			biderphone = self.db.query_db(bider_query, info)
			
			ACCOUNT_SID = "AC6299d9965195b73c17cc2b122f001981" 
			AUTH_TOKEN = "f5aaa6ee4c008c0606efa4e27a4417b4" 

			client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

			client.messages.create(
				to="+1"+biderphone[0]['phone'],
				# to="+13016613576",
				# to="+18015809898", 
				from_="+16572209489", 
				body="Your bid has been accepted on "+employerinfo[0]['title'] + " by " + employerinfo[0]['firstname']+ " " + employerinfo[0]['lastname'],
				media_url="http://farm2.static.flickr.com/1075/1404618563_3ed9a44a3a.jpg"
			)
			# Send acceptance SMS to user where user.id = :user_id
		elif info['status']== '1' and prev_status[0]['status'] == 2:
			resetquery = "UPDATE bids SET status= 0, updated_at= NOW() WHERE job_id = :job_id AND id != :id"
			self.db.query_db(resetquery, info)
			jobsquery = "UPDATE jobs SET status = 'open', updated_at = NOW() WHERE id= :job_id"
			self.db.query_db(jobsquery, info)
		return {'status': True, 'job_id': requestform['job_id']}

	def destroy_bid(self, requestform):
		info = {
    	'id': requestform['id'],
    	'job_id': requestform['job_id']
    	}
		print "THIS IS DESTRUCTIVE"
		query = "DELETE FROM bids WHERE id = :id"
		self.db.query_db(query, info)
		return {'status': True, 'job_id': requestform['job_id']}
