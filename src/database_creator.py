import sqlite3
import queries


def main():
    create_database(queries.create_author_database, 'authors')
    create_database(queries.create_events_database, 'events')


def create_database(query, database_name):
    try:
        sqlite_connection = sqlite3.connect(f'../db/{database_name}.db')
        cursor = sqlite_connection.cursor()

        cursor.executescript(query)
        sqlite_connection.commit()

        cursor.close()
        sqlite_connection.close()

        print(f"База данных {database_name} создана")

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
        exit()


if __name__ == "__main__":
    main()
