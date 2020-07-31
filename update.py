import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  # host="10.2.1.127",
                                  port="5432",
                                  database="sf_test")
    cursor = connection.cursor()

    # добавление новых строк
    postgres_insert_query = """
    INSERT INTO mobile (ID, MODEL, PRICE)
    VALUES (%s, %s, %s)
    """
    records_to_insert = [
        (1, "Iphone XS", 1050),
        (2, "Nutella", 30),
        (3, "Pixel", 970),
    ]
    for record in records_to_insert:
        cursor.execute(postgres_insert_query, record)

    # обновление строк
    postgres_update_query = """
    UPDATE mobile SET price = 900
    WHERE price > 900
    """
    cursor.execute(postgres_update_query)
    connection.commit()
    # print(mobile_records)
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")