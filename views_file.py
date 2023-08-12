import mysql.connector

def create_mysql_connection():
    try:
        conn_mysql = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kunjara123@",
            database = "Automobile"
        )
        print("MySQL connection created")
        return conn_mysql

    except mysql.connector.Error as e:
        print("MySQL connection error:", e)


# Creating the MySQL connection
conn_mysql = create_mysql_connection()

cursor = conn_mysql.cursor()


try:
    create_view_query = "CREATE VIEW second_view AS SELECT * FROM insurance limit 10"

    cursor.execute(create_view_query)

    conn_mysql.commit()

    print("View 'second_view' created successfully!")

except mysql.connector.Error as error:
        print("Error occurred while executing the create view query:", error)

cursor.close()
conn_mysql.close()







