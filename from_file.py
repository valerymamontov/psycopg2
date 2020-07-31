import psycopg2
from pprint import pprint

try:
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  # host="10.2.1.127",
                                  port="5432",
                                  database="sf_test")
    cursor = connection.cursor()
    with open("mobile.csv", "r") as file:
        cursor.copy_from(file, "mobile", sep=",")
    connection.commit()

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
