from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

    def show_users(self):

    	# user list

    def show_user(self, u_id):

    	# user dashboard profile editor, show user page

    def show_addresses(self, u_id):

    	# user dashboard profile editor

    def show_address(self, address_id):

    	# job page

    def userlogin(self):

    	#POST pass requestform to Model login
    	#set session

    def useradd(self):

    	# POST pass requestform to Model add
    	#set session

    def userupdate(self):

    	# POST pass requestform to model update

    def pwupdate(self):

    	#POST pass pw to Model

    def addaddress(self):

    	#Insert new address, addresses can be added or deleted.
    	#Delete removes foreign key assignment

    def removeuser(self):

    	#admin only, passes requestform  

    def removeaddress(self):

    	#passes requestform
