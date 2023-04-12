import sqlite3
import queries
import csv


def main():
    try:
        blog_conection = sqlite3.connect('../db/blog.db')
        blog_cursor = blog_conection.cursor()

        events_connection = sqlite3.connect('../db/events.db')
        events_cursor = events_connection.cursor()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
        return

    user_login = input('Введите имя пользователя для получения статистики:')

    user_id_query = queries.get_user_id_by_login.format(user_login)
    blog_cursor.execute(user_id_query)

    result = blog_cursor.fetchone()
    if result is None:
        print(f'Пользователь с логином "{user_login}" не найден')
        exit()

    user_id = result[0]

    parse_to_file(user_id, queries.select_comments_info_by_user_id, blog_cursor, 'comment_info')
    parse_to_file(user_id, queries.select_event_by_user, events_cursor, 'events_info')

    print('Статистика выведена в папку csv')


def parse_to_file(user_id, query, cursor, filename):
    comments_info_query = query.format(user_id)

    cursor.execute(comments_info_query)
    result = cursor.fetchall()

    with open(f'..\csv\{filename}.csv', 'w', newline='') as file:
        writer = csv.writer(file, )
        for row in result:
            writer.writerow(row)


if __name__ == "__main__":
    main()
