from Sql import SqlRegister as sr

def num_total_users():

    total_number = list(sr.SqlRegister().total_users())[0][0]

    return total_number


def is_user_exists(user):

    return True if sr.SqlRegister().record_exist(user) else False


def insert_user(username, password, first_name, last_name, mail):

    sr.SqlRegister().insert_user_record(username, password, first_name, last_name, mail)
