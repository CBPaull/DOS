from system.core.model import Model
import re
# still need to import this module: we use regular expressions to validate email formats!

class Bid(Model):

	def show_job_bids(self, job_id):
		info = { 'job_id': job_id }
		query = "SELECT bids.id AS id, bids.price AS price, bids.comment AS comment, bids.created_at AS created_at, users.firstname AS firstname, users.lastname AS lastname FROM jobs JOIN bids ON jobs.id = bids.job_id JOIN users ON bids.user_id = users.id WHERE jobs.id = :job_id ORDER BY bids.created_at DESC"
		bids = self.db.query_db(query, info)
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
		query = " INSERT INTO bids(price, comment, status, job_id, user_id, created_at, updated_at) VALUES(:price, :comment, :status, :job_id, user_id, NOW(), NOW())"
		self.db.query_db(query, info)
		return {'status': True, 'job_id': requestform['job_id']}

	def change_bid_status(self, requestform):
		info = {
    		'id': requestform['id'],
    		'status': requestform['status'],
    		'user_id': requestform['user_id'],
    		'job_id': requestform['job_id']
    	}
		query = "UPDATE bids SET status= :status, updated_at= NOW() WHERE id = :id"
		self.db.query_db(query, info)
		if info['status']== '2':
			rejectquery = "UPDATE bids SET status= 1, updated_at= NOW() WHERE job_id = :job_id AND id != :id"
			self.db.query_db(rejectquery, info)
		# Send acceptance SMS to user where user.id = :user_id
 		return {'status': True, 'job_id': requestform['job_id']}

	def destroy_bid(self, requestform):
		info = {
    	'id': requestform['id']
    	}
		query = "DELETE FROM bids WHERE id = :id"
		self.query_db(query, info)
		return {'status': True, 'job_id': requestform['job_id']}
