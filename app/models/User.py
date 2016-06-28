from system.core.model import Model
import re     # still need to import this module: we use regular expressions to validate email formats!
class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def login_user(self, requestform):
        info = {
            'email': requestform['email'],
            'password': requestform['password']
        }
        errors = []
        user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        user_data = {'email': info['email']}
        user = self.db.query_db(user_query, user_data)
        if user:
           # check_password_hash() compares encrypted password in DB to one provided by user logging in
            if self.bcrypt.check_password_hash(user[0]['pw_hash'], info['password']):
                return { "status": True, "user": user[0]}
        else:
            errors.append('Incorrect Email or Password')
            return {"status": False, "errors": errors}

    def add_user(self, requestform):
        info = {
            'firstname': requestform['firstname'],
            'lastname': requestform['lastname'],
            'email': requestform['email'],
            'phone': requestform['phone'],
            'password': requestform['password'],
            'confirmation': requestform['confirmation'],
            'user_level': requestform['user_level']

        }
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        PASS_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')
        USER_REGEX = re.compile(r'^[a-zA-Z]+$')
        errors = []
        # Some basic validation
        if not info['firstname']:
            errors.append('First name cannot be blank')
        elif len(info['firstname']) < 2:
            errors.append('first name must be at least 2 characters long')
        elif not USER_REGEX.match(info['firstname']):
            errors.append('first name can contain only letters')
        if not info['lastname']:
            errors.append('Last name cannot be blank')
        elif len(info['lastname']) < 2:
            errors.append('Last name must be at least 2 characters long')
        elif not USER_REGEX.match(info['firstname']):
            errors.append('first name can contain only letters')
        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')
        if not info['password']:
            errors.append('Password cannot be blank')
        elif len(info['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif not PASS_REGEX.match(info['password']):
            errors.append('Password must contain an uppercase letter and a number')
        elif info['password'] != info['confirmation']:
            errors.append('Password and confirmation must match!')
        # If we hit errors, return them, else return True.
        if errors:
            return {"status": False, "errors": errors}
        else:
            pw_hash = self.bcrypt.generate_password_hash(info['password'])
            insert_query = "INSERT INTO users (firstname, lastname, email, phone, pw_hash, created_at, updated_at) VALUES (:firstname, :lastname, :email, :phone, :pw_hash, NOW(), NOW())"
            data = { 'firstname': info['firstname'], 'lastname': info['lastname'], 'email': info['email'], 'phone': info['phone'], 'pw_hash': pw_hash }
            print data
            self.db.query_db(insert_query, data)
            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)

        address = {
            'address1': requestform['address1'],
            'city': requestform['city'],
            'zipcode': requestform['zipcode'],
            'apartment': requestform['apartment'],
            'home': requestform['home']
        }
        # still need a check to ensure address is correct.
        address_query = "INSERT INTO Addresses (address1, city, zipcode, apartment, created_at, updated_at) VALUES (:address1, :city, :zipcode, :apartment, NOW(), NOW())"
        address_data = {'address1': address['address1'], 'city': address['city'], 'zipcode': address['zipcode'], 'apartment': address['apartment'] }
        self.db.query_db(address_query, address_data)
        get_address_query = "SELECT * FROM addresses ORDER BY id DESC LIMIT 1"
        user_address = self.db.query_db(get_address_query)
        link_query = "INSERT INTO Users_has_Addresses (Users_id, Addresses_id) VALUES ( :Users_id, :Addresses_id)"
        link_data = { 'Users_id': users[0]['id'], 'Addresses_id': user_address[0]['id']}
        self.db.query_db(link_query, link_data)
        return { "status": True, "user": users[0]}

    def update_user(self, requestform):
        info = {
            'firstname': requestform['firstname'],
            'lastname': requestform['lastname'],
            'email': requestform['email'],
            'phone': requestform['phone'],
            'servicename': requestform['servicename'],
            'user_level': requestform['user_level']
        }
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        USER_REGEX = re.compile(r'^[a-zA-Z]+$')
        errors = []
        if not info['firstname']:
            errors.append('First name cannot be blank')
        elif len(info['firstname']) < 2:
            errors.append('first name must be at least 2 characters long')
        elif not USER_REGEX.match(info['firstname']):
            errors.append('first name can contain only letters')
        if not info['lastname']:
            errors.append('Last name cannot be blank')
        elif len(info['lastname']) < 2:
            errors.append('Last name must be at least 2 characters long')
        elif not USER_REGEX.match(info['firstname']):
            errors.append('first name can contain only letters')
        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')
        if errors:
            return {"status": False, "errors": errors, "user_id": info['id']}
        else:
            query = "UPDATE users SET firstname=:firstname, lastname=:lastname, email=:email, phone=:phone, servicename=:servicename, user_level=:user_level, updated_at=NOW() WHERE id=:id"
            self.db.query_db(query, info)
            return {"status": True, "id": info['id']}

    def pw_update(self, requestform):
        info = {
            'password': requestform['password'],
            'confirmation': requestform['confirmation'],
            'id': requestform['id']
        }
        errors = []
        PASS_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')
        if not info['password']:
            errors.append('Password cannot be blank')
        elif len(info['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif not PASS_REGEX.match(info['password']):
            errors.append('Password must contain an uppercase letter and a number')
        elif info['password'] != info['confirmation']:
            errors.append('Password and confirmation must match!')
        # If we hit errors, return them, else return True.
        if errors:
            return {"status": False, "errors": errors, "user_id": info['id']}
        else:
            pw_hash = self.bcrypt.generate_password_hash(info['password'])
            query = "UPDATE users SET pw_hash= pw_hash WHERE id=:id"
            self.db.query_db(query, info)
            return {"status": True, "id": info['id']}

    def address_update(self, requestform, user_id):
        address = {
            'address1': requestform['address1'],
            'city': requestform['city'],
            'zipcode': requestform['zipcode'],
            'apartment': requestform['apartment'],
            'home': requestform['home']
        }
        address_query = "UPDATE address SET address1=:address1, city=:city, zipcode=:zipcode, apartment=:apartment, home=:home, updated_at=NOW() WHERE id=:id"
        address_data = {'address1': address['address1'], 'city': address['city'], 'zipcode': address['zipcode'], 'apartment': address['apartment'] }
        self.db.query_db(address_query, address_data)
        get_address_query = "SELECT * FROM addresses ORDER BY id DESC LIMIT 1"
        user_address = self.db.query_db(get_address_query)
        link_query = "INSERT INTO Users_has_Addresses (Users_id, Addresses_id) VALUES ( :Users_id, :Addresses_id)"
        link_data = {'Users_id': user_id, 'Addresses_id': user_address[0]['id']}
        self.db.query_db(link_query, link_data)
        return {"status": True, "user_id": user_id}

    def delete_user(self, requestform):
        info = {
            'id': requestform['user_id']
        }
        query = 'DELETE FROM users WHERE id=:id'
        self.db.query_db(query, info)
        status = 'success'
        return status

