import mysql.connector

def create_mysql_connection():
    try:
        conn_mysql = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kunjara123@",
            database = "Student"
        )
        print("MySQL connection created")
        return conn_mysql

    except mysql.connector.Error as e:
        print("MySQL connection error:", e)


# Creating the MySQL connection
conn_mysql = create_mysql_connection()

cursor = conn_mysql.cursor()
# Getting all the table names
cursor.execute('SHOW TABLES;')
table_names = []
for record in cursor.fetchall():
    table_names.append(record[0])
  
backup_dbname = "Student" + '_backup'
try:
    cursor.execute(f'CREATE DATABASE {backup_dbname}')
except:
    pass
  
cursor.execute(f'USE {backup_dbname}')
  
for table_name in table_names:
    cursor.execute(
        f'CREATE TABLE {table_name} SELECT * FROM {"Student"}.{table_name}')
