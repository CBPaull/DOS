from system.core.model import Model
import re
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
