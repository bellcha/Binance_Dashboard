from mysql.connector import MySQLConnection, Error
from mysql_config import read_config


def connect():
    """ Connect to MySQL database """

    db_config = read_config()
    conn = None
    try:
        print('Connecting to MySQL database...')
        
        conn = MySQLConnection(**db_config).connect()
        
        print("MySQL Database connection successful")

    except Error as error:
        print(f'Error: {error}')
    
    return conn


if __name__ == '__main__':
    connect()