from Sql import SqlUser as su

class User:

    username = ''
    first_name = ''
    last_name = ''
    email = ''
    password = ''

class UserController:

    def __init__(self, username):

        self.username = username
        self.user = User()

    def get_user(self):

        raw_data = su.SqlRegister(self.username).get_user_record()[0]
        self.user.username = raw_data[0]
        self.user.first_name = raw_data[1]
        self.user.last_name = raw_data[2]
        self.user.email = raw_data[3]
        self.user.password = raw_data[4]

        return self.user
