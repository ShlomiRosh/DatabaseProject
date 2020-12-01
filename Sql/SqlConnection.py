import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="5678910",
    database="sql_invoicing"
)
# mycursor = mydb.cursor()
# sql = "INSERT INTO users (username, firstname, lastname, email, password) VALUES (%s, %s, %s, %s, %s)"
# val = ('1234rtty', 'fj', 'au', 'r23t@mail.project', '1239886')
# mycursor.execute(sql, val)
# mydb.commit()
#
# print(mycursor.rowcount, "record inserted.")

def has_record(user, password):

    mycursor = mydb.cursor()
    sql = "SELECT username, COUNT(*) FROM users WHERE username = %s and password = %s GROUP BY username"
    #sql = "SELECT COUNT(username) FROM users WHERE username LIKE %s AND password LIKE %s"
    adr = (user, password)
    mycursor.execute(sql, adr)

    return mycursor.fetchall()

#print(has_record("Johnqwer", "123456"))

def total_users():

    mycursor = mydb.cursor()
    mycursor.execute("select count(*) from users")
    #print(type(list(mycursor)[0]))
    return list(mycursor)[0][0]

#print(total_users())

def is_exists_user(user):

    mycursor = mydb.cursor()
    sql = "SELECT username FROM users WHERE users.username LIKE %s"
    # sql = "SELECT COUNT(username) FROM users WHERE username LIKE %s AND password LIKE %s"
    adr = (user,)
    mycursor.execute(sql,adr)

    return mycursor.fetchall()

print(is_exists_user("Johnqwer"))