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
            with self.conn.cursor() as curcor:
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
            self.conn.commit()
            return 'Created new user'
        

    def getAllUsers(self):
        try:
            with self.conn.cursor() as curcor:
                sql = f'''
                    SELECT * FROM user;
                '''
                curcor.execute(sql)
                data = curcor.fetchall()
        except Exception as err:
            return err
        else:
            return data



