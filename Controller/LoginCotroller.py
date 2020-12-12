from Sql import SqlLogin as sl

class LoginController:

    def __init__(self, user, password):

        self.user = user
        self.password = password
        self.sql_login = sl.SqlLogin(self.user, self.password)

    def has_user(self):

        res = self.sql_login.has_record()
        if res == 'Error':
            return 'Error Connection'
        return True if res[0][0] != 0 else False


