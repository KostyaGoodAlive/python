
import psycopg2

def add_to_database(item: dict):
    try:
        connection = psycopg2.connect(
            user='KostyaGoodAlive',
            database='neondb',
            password='TL6XKA4fkVqN',
            host='ep-restless-butterfly-233506.eu-central-1.aws.neon.tech',
            port='5432'
        )

        cursor = connection.cursor()
    

        columns = ', '.join(item.keys())
        print(columns)

        values = ', '.join(['%s'] * len(item))

        print(values)
        """
        INSERT INTO devices (column1, column2, column3) VALUES (%s, %s, %s)
        """

        insert_query = f"INSERT INTO devices ({columns}) VALUES ({values})"
        cursor.execute(insert_query, list(item.values()))
        connection.commit()

        print('Success')
    except Exception as e:
        print(e)


test = {'name': 'Смартфон Apple iPhone 14 Pro Max 1Tb Deep Purple', 'code': '2149521', 'old_price': 82999, 'current_price': 79999, 'reviews': 13}

add_to_database(test)
        