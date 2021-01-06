from Db import SqlLogin as sl

# This class is responsible for the page Login.
class LoginController:

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.sql_login = sl.SqlLogin(self.user, self.password)

    # Asks SQL if there is a user with this name, answers according to the information received from SQL.
    def has_user(self):
        res = self.sql_login.has_record()
        if res == 'Error':
            return 'Error Connection'
        return True if res[0][0] != 0 else False


