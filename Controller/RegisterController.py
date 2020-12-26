from Sql import SqlRegister as sr
# This module is responsible for the page register.

# Returns the number of registered users by accessing SQL.
def num_total_users():
    res = sr.SqlRegister().total_users()
    return 'Error Connection' if res == 'Error' else list(res)[0][0]

def is_user_exists(user):
    res = sr.SqlRegister().record_exist(user)
    if res == 'Error':
        return 'Error Connection'
    return True if res else False

# Turns to SQL and adds a new user to the database.
def insert_user(username, password, first_name, last_name, mail):
    res = sr.SqlRegister().insert_user_record(username, password, first_name, last_name, mail)
    return 'Error Connection' if res == 'Error' else 'Inserted'
