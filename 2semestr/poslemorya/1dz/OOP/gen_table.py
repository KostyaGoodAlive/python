import psycopg2


def registration():
    try:
        connection = psycopg2.connect(
            host='ep-restless-butterfly-233506.eu-central-1.aws.neon.tech',
            port='5432',
            database='neondb',
            user='KostyaGoodAlive',
            password='TL6XKA4fkVqN'
        )

        cursor = connection.cursor()

        query = 'INSERT INTO students (name, age, email) VALUES (%s, %s, %s)'
        cursor.execute(query, ('name', 'age', 'email'))
        connection.commit()

        print('Student successfully registered!')
    except Exception as error:
        print('An error occurred while registering user: ', error)
    finally:
        if connection:
            connection.close()
            cursor.close()


registration()