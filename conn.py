
import pymysql


def connect_to_db():
    try:
    # Open a database connection
        #connection = pymysql.connect( host = 'localhost', user = 'postgres', password = 'postgres', database = 'db_design_project2')
        
        connection = pymysql.connect(
            host='localhost',
            user='phpmyadmin',
            passwd='123',
            db='test_inserts'
        )
        
        return connection
    except:

        print(f"An exception occurred: {connection}")