import psycopg2


def replasce(email: str, new_age: int):
    try:    
        connection = psycopg2.connect(
            host='ep-restless-butterfly-233506.eu-central-1.aws.neon.tech',
            port='5432',
            database='neondb',
            user='KostyaGoodAlive',
            password='TL6XKA4fkVqN'
        )
        cursor = connection.cursor()

        query = 'SELECT * FROM students WHERE email = %s'
        cursor.execute(query, (email))
        user = cursor.fetchone()

        if user:
            user_id = user[0]
            update_query = 'UPDATE students WHERE id = %s'
            cursor.execute(update_query, (user_id))
            connection.commit()
            print('User found!')
        else:
            print('User not found:(')

        cursor.close()
        connection.close()

    except Exception as error:
        print('An error:', error)


if __name__ == "__main__":
    email = input('Email: ')
    replasce(email)