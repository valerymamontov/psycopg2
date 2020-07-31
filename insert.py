import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  # host="10.2.1.127",
                                  port="5432",
                                  database="sf_test")
    cursor = connection.cursor()

    postgres_insert_query = """ 
    INSERT INTO mobile (ID, MODEL, PRICE)
    VALUES(%s, %s, %s)
    """
    record_to_insert = (5, "One Plus 6", 950)

    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    count = cursor.rowcount # count будет равен 1
    print(count, "Record inserted successufully into mobile table")
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
