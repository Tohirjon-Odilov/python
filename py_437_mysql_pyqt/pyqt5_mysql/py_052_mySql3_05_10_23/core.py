import mysql.connector


class Core:

    def __init__(self) -> None:
        self.__dbConection()

    def __dbConection(self):
        try:
            self.connect = mysql.connector.connect(
                host='localhost',
                database='chatdb',
                user='root',
                password='root'
            )
        except Exception as err:
            print(err)
        else:
            print('Database connection is successful')

    def createUser(self, user):
        try:
            with self.connect.cursor() as curcor:
                sql = f'''
                    INSERT INTO user (full_name, user_name, password, mobile_number) 
                    VALUES (
                        "{user['full name']}", 
                        "{user['username']}", 
                        "{user['password']}", 
                        "{user['mobile number']}"
                        );
                '''
                curcor.execute(sql)

        except Exception as err:
            return err
        else:
            self.connect.commit()
            return 'Created new user'

    def getAllUsers(self):
        try:
            with self.connect.cursor() as curcor:
                sql = f'''
                    SELECT * FROM user;
                '''
                curcor.execute(sql)
                data = curcor.fetchall()
        except Exception as err:
            return err
        else:
            return data
        
    def updatedUser(self, user):
        print(user)
        try:
            with self.connect.cursor() as cursor:
                sql = f'''
                    UPDATE user SET 
                    full_name = "{user['full name']}", 
                    user_name = "{user['username']}", 
                    password = "{user['password']}", 
                    mobile_number = "{user['mobile number']}"
                    WHERE id = {user['user id']};
                '''
                print(sql)
                cursor.execute(sql)
        except Exception as err:
            return err
        else:
            self.connect.commit()
            return "Updated user"
        
    def deletedUser(self, enteredId):
        try:
            with self.connect.cursor() as cursor:
                sql = f'''
                    DELETE FROM user 
                    WHERE id = '{enteredId}';   
                '''
                cursor.execute(sql)

        except Exception as err:
            return err
        else:
            self.connect.commit()
            return 'Deleted user'
