from system.core.model import Model

class Review(Model):

    def __init__(self):
        super(Review, self).__init__()

    def create_review(self, input_form):
        data = {
            'overall': input_form['overall'],
            'review': input_form['review_text'],
            'job_id': input_form['job_id'],
            'to_user_id': input_form['to_user_id'],
            'user_id': input_form['user_id']
        }
        query = "INSERT INTO reviews(overall, review, job_id, to_user_id, user_id, created_at, updated_at) " \
                "VALUES(:overall, :review, :job_id, :to_user_id, :user_id, NOW(), NOW());"
        review_id = self.db.query_db(query, data)
        return {'status': True}

    def get_reviews_for_id(self, user_id):
        # Get all reviews, for a user_id based on job_id they posted.
        data = {
            "user_id": str(user_id)
        }
        query = "SELECT reviews.overall, reviews.review, reviews.user_id, users.firstname AS 'firstname', " \
                "users.lastname AS 'lastname', jobs.title AS 'title' " \
                "FROM reviews " \
                "JOIN users ON reviews.user_id = users.id " \
                "JOIN jobs ON reviews.job_id = jobs.id " \
                "WHERE to_user_id=:user_id; "
        reviews = self.db.query_db(query, data)
        return reviews

    # def get_reviews_by_id(self, user_id):
        # Get all reviews a user_id wrote.