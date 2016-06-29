from system.core.model import Model
import re     # still need to import this module: we use regular expressions to validate email formats!

class Bid(Model):

	def show_job_bids(self, job_id):
		info = { 'job_id': job_id }
        query = "SELECT bids.price AS price, bids.comment AS comment, bids.created_at AS created_at, users.firstname AS firstname, users.lastname AS lastname FROM jobs " \
                "LEFT JOIN bids ON jobs.id = bids.job_id "\
                "LEFT JOIN users ON bids.user_id = users.id " \
                "WHERE jobs.id = :job_id"
        addresses = self.db.query_db(query, info)
        return addresses