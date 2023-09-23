from mysql.connector import connect, Error
from crud import create_database_query

try:
    with connect(host="localhost", user="admin", password="admin", port="3306") as conn:
        with conn.cursor() as cursor:
            cursor.execute(create_database_query)

except Error as e:
    print(e)
