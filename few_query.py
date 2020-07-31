import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  # host="10.2.1.127",
                                  port="5432",
                                  database="sf_test")
    cursor = connection.cursor()
    # 1. удалим все данные
    # cursor.execute("DELETE FROM mobile")

    # 2. вставим новые данные
    # insert_query = "INSERT INTO mobile (id, model, price) VALUES (%s, %s, %s)"
    # records_to_insert = [
    #     (1, "Iphone XS", 1050),
    #     (2, "Nutella", 30),
    #     (3, "Pixel", 970),
    # ]
    # cursor.executemany(insert_query, records_to_insert)

    # 3. теперь используем psycopg2 для вставки
    # update_query = "UPDATE mobile SET model = %s WHERE model = %s"
    # records_to_update = [
    #     ("Nutella", "Iphone XS",),
    #     ("Nutella", "Pixel",),
    # ]
    # cursor.executemany(update_query, records_to_update)

    # 4. удаление нескольких строк
    # найдём список цен, которые не удовлетворяют нашему условию
    cursor.execute("SELECT price FROM mobile WHERE price not between 900 and 1000")
    records_to_delete = cursor.fetchall()

    # теперь удалим строки с найденными ценами
    delete_query = "DELETE FROM mobile WHERE price = %s"
    cursor.executemany(delete_query, records_to_delete)
    connection.commit()

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
