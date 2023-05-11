import mysql.connector

def authenticate_user(username, password):

    database = mysql.connector.connect(user='db_admin', host='127.0.0.1', 
                                    password='1pa$$WORD12345', port=23, 
                                    auth_plugin='mysql_native_password')


    

    cursor = database.cursor(dictionary=True)
    cursor.execute("USE production_db;")
    cursor.execute("select * from credentials where username = %s and password = %s", 
                [username, password])

    result = cursor.fetchall()
    if len(result) > 0:
        return True
    
if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    authenticate_user(username=username, password=password)