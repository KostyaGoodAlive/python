import psycopg2
from getpass import getpass


def registration():
    username = input('Username: ')
    password = getpass()
    email = input('Email: ')

    try:
        connection = psycopg2.connect(
            host='ep-restless-butterfly-233506.eu-central-1.aws.neon.tech',
            port='5432',
            database='neondb',
            user='KostyaGoodAlive',
            password='TL6XKA4fkVqN'
        )

        cursor = connection.cursor()

        query = 'INSERT INTO users (username, password, email) VALUES (%s, %s, %s)'
        cursor.execute(query, (username, password, email))

        user = cursor.fetchone()
        print(user)
        if user:
            print('User alredy registred , pls login')
        else:
            print('User successfully registered!')

        cursor.close()
        connection.close()

    except Exception as error:
        print('An error occurred while registering user: ', error)


def login():
    email = input('Email: ')
    password = getpass()

    try:
        connection = psycopg2.connect(
            host='ep-restless-butterfly-233506.eu-central-1.aws.neon.tech',
            port='5432',
            database='neondb',
            user='KostyaGoodAlive',
            password='TL6XKA4fkVqN'
        )

        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))

        user = cursor.fetchone()
        print(user)

        if user:
            print('You have logged in!')
        else:
            print('Invalid login credentials.')

    except Exception as error:
        print('An error occurred while logging: ', error)
    finally:
        connection.close()
        cursor.close()
    


if __name__ == '__main__':
    match input('Select an action: (register/login)'):
        case 'login':
            login()
        case 'register':
            registration()
        case _:
            print('invalid action.')        