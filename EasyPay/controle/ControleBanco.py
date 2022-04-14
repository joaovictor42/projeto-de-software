import sqlite3


class ConnEasyPayDB:

    @staticmethod
    def create_database():
        create_table_sql = '''
            CREATE TABLE USUARIOS (
                ID INTEGER PRIMARY KEY,
                LOGIN TEXT NOT NULL,
                SENHA TEXT NOT NULL
            );
        '''
        ConnEasyPayDB.execute_sql(create_table_sql)
    
    @staticmethod
    def execute_sql(sql, params=''):
        conn = sqlite3.connect('EasyPay.db')
        try:
            cursor = conn.cursor()
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            conn.commit()
            cursor.close() 
        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if conn:
                conn.close()

if __name__ == '__main__':
    ConnEasyPayDB.create_database()