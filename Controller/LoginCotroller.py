from Sql import SqlLogin as sl

class LoginController:

    def __init__(self, user, password):

        self.user = user
        self.password = password
        self.sql_login = sl.SqlLogin(self.user, self.password)

    def has_user(self):

        return True if self.sql_login.has_record() else False



