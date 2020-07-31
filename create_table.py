# Пример транзакции
# Сделаем новую таблицу в виде транзакции:
import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database="sf_test")
    cursor = connection.cursor()

    create_table_query = '''CREATE TABLE mobile 
          (ID INT PRIMARY KEY     NOT NULL, 
          MODEL           TEXT    NOT NULL, 
          PRICE         REAL); '''

    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL ")
except (Exception, psycopg2.DatabaseError) as error:
    print("Error while creating PostgreSQL table", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
