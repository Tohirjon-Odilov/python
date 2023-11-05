import mysql.connector

class Core:
    
    def __init__(self) -> None:
        self.__dbConection()

    def __dbConection(self):
        try:
            self.conn = mysql.connector.connect(
                host = 'localhost',
                database = 'chatdb',
                user = 'root',
                password = 'root'
            )
        except Exception as err:
            print(err)
        else:
            print('Database connection is successful')

    def createUser(self, user):
        try:
            with self.conn.cursor() as cursor:
                sql = f'''
                    INSERT INTO user (full_name, user_name, password, mobile_number) 
                    VALUES (
                        '{user['full name']}', 
                        '{user['username']}', 
                        '{user['password']}', 
                        '{user['mobile number']}')
                '''
                cursor.execute(sql)
        except Exception as err:
            print(err)
            return err
        else:
            self.conn.commit()
            return 'New user created successfully'
        
    def getAllUsers(self):
        try:
            with self.conn.cursor() as cursor:
                query = f'''SELECT * FROM user'''
                cursor.execute(query)
                result = cursor.fetchall()
        except Exception as err:
            print(err)
            return err
        else:
            return result        

    def setUser(self, user):
        try:
            with self.conn.cursor() as cursor:
                sql = f'''
                    UPDATE user SET full_name = '{user['full name']}', 
                    user_name = '{user['username']}', 
                    password = '{user['password']}', 
                    mobile_number = '{user['mobile number']}' 
                    WHERE id = {user['id']}
                '''
                cursor.execute(sql)
        except Exception as err:
            print(err)
            return err
        else:
            self.conn.commit()
            return 'User updated successfully'