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

    postgres_select_query = """
    SELECT * FROM mobile
    """
    cursor.execute(postgres_select_query)
    mobile_records = cursor.fetchall()
    connection.commit()
    pprint(mobile_records)
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
