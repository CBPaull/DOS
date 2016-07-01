from system.core.model import Model

    class Email(Model):

        def __init__(self):
            super(Email, self).__init__()

        def send_review_emails(self, users, job):
            # Send emails to poster and contractor
            email_poster = users['user']['email']
            email_contractor = users['accepted']['email']
            self.send_contractor(email_contractor, job)



        def send_contractor(self, contractor_email, job):
            return requests.post(
                "https://api.mailgun.net/v3/samples.mailgun.org/messages",
                auth=("api", "key-3ax6xnjp29jd6fds4gc373sgvjxteol0"),
                data={"from": "DOS",
                      "to": ["devs@mailgun.net"],
                      "subject": "Congratulations on a job done!",
                      "text": "Please review your job here!  "})