import sqlite3


def main():
    fill_blog()
    fill_logs()


def fill_blog():
    try:
        sqlite_connection = sqlite3.connect(f'../db/blog.db')
        cursor = sqlite_connection.cursor()
    except sqlite3.Error as error:
        print("Не удалось подключиться к базе ", error)
        return

    users = [
        ('user1@example.com', 'user1'),
        ('user2@example.com', 'user2'),
        ('user3@example.com', 'user3'),
        ('user4@example.com', 'user4')
    ]

    blogs = [
        (1, 'user1_blog', 'user1_blog_description'),
        (2, 'user2_blog', 'user2_blog_description'),
        (3, 'user3_blog', 'user3_blog_description'),
        (4, 'user1_blog', 'user4_blog_description')
    ]

    posts = [
        ('user1_post_1_header', 'post_text', 1, 1),
        ('user1_post_2_header', 'post_text', 1, 1),
        ('user1_post_3_header', 'post_text', 1, 1),
        ('user1_post_4_header', 'post_text', 1, 1),
        ('user2_post_1_header', 'post_text', 2, 2),
        ('user2_post_2_header', 'post_text', 2, 2),
        ('user4_post_1_header', 'post_text', 4, 4),
        ('user4_post_2_header', 'post_text', 4, 4),
        ('user4_post_3_header', 'post_text', 4, 4),
        ('user4_post_4_header', 'post_text', 4, 4),
        ('user4_post_5_header', 'post_text', 4, 4),
        ('user4_post_6_header', 'post_text', 4, 4),
        ('user4_post_7_header', 'post_text', 4, 4),
        ('user4_post_8_header', 'post_text', 4, 4),
        ('user4_post_9_header', 'post_text', 4, 4),
        ('user4_post_10_header', 'post_text', 4, 4),
        ('user4_post_11_header', 'post_text', 4, 4),
    ]

    comments = [
        ('comment_text', 1, 1),
        ('comment_text', 1, 1),
        ('comment_text', 1, 1),
        ('comment_text', 2, 3),
        ('comment_text', 2, 4),
        ('comment_text', 1, 2),
        ('comment_text', 3, 5),
        ('comment_text', 3, 5),
        ('comment_text', 3, 5),
        ('comment_text', 4, 6),
        ('comment_text', 1, 3),
        ('comment_text', 2, 7),
        ('comment_text', 2, 7),
        ('comment_text', 2, 7),
        ('comment_text', 3, 8),
        ('comment_text', 4, 9),
        ('comment_text', 4, 9),
        ('comment_text', 4, 9),
        ('comment_text', 1, 4),
        ('comment_text', 2, 10),
        ('comment_text', 3, 11),
        ('comment_text', 3, 11),
        ('comment_text', 3, 11),
        ('comment_text', 4, 12),
        ('comment_text', 1, 5),
        ('comment_text', 2, 6),
        ('comment_text', 3, 7),
        ('comment_text', 3, 7),
        ('comment_text', 3, 7),
        ('comment_text', 3, 7),
        ('comment_text', 3, 7),
        ('comment_text', 4, 8),
        ('comment_text', 1, 6),
        ('comment_text', 2, 9),
        ('comment_text', 3, 10),
        ('comment_text', 4, 11),
        ('comment_text', 1, 7),
        ('comment_text', 1, 7),
        ('comment_text', 1, 7),
        ('comment_text', 2, 8),
        ('comment_text', 2, 8),
        ('comment_text', 2, 8),
        ('comment_text', 3, 9),
        ('comment_text', 4, 12),
        ('comment_text', 1, 8),
        ('comment_text', 2, 11),
        ('comment_text', 3, 12),
        ('comment_text', 4, 5),
        ('comment_text', 1, 9),
        ('comment_text', 1, 9),
        ('comment_text', 1, 9),
        ('comment_text', 2, 6),
        ('comment_text', 3, 7),
        ('comment_text', 4, 8),
        ('comment_text', 4, 8),
        ('comment_text', 4, 8),
        ('comment_text', 1, 10),
        ('comment_text', 2, 9),
        ('comment_text', 2, 9),
        ('comment_text', 2, 9),
        ('comment_text', 3, 11),
        ('comment_text', 4, 12),
    ]

    try:
        cursor.executemany('INSERT INTO users (email, login) VALUES (?, ?)', users)
        cursor.executemany('INSERT INTO blog (owner_id, name, description) VALUES (?, ?, ?)', blogs)
        cursor.executemany('INSERT INTO post (header, text, author_id, blog_id) VALUES (?, ?, ?, ?)', posts)
        cursor.executemany('INSERT INTO comment (text, user_id, post_id) VALUES (?, ?, ?)', comments)
    except sqlite3.Error as error:
        print("Не удалось вставить значения", error)
        return

    sqlite_connection.commit()
    cursor.close()
    sqlite_connection.close()
    print('База блога заполнена значенями')


def fill_logs():
    try:
        sqlite_connection = sqlite3.connect(f'../db/events.db')
        cursor = sqlite_connection.cursor()
    except sqlite3.Error as error:
        print("Не удалось подключиться к базе ", error)
        return

    logs = [
        ('2023-04-01 12:30:00', 1, 1, 1),
        ('2023-04-02 09:15:00', 1, 1, 5),
        ('2023-04-03 16:45:00', 1, 1, 1),
        ('2023-04-01 08:00:00', 1, 1, 5),
        ('2023-04-02 14:30:00', 1, 1, 1),
        ('2023-04-03 12:15:00', 1, 2, 3),
        ('2023-04-01 16:30:00', 1, 2, 3),
        ('2023-04-02 11:45:00', 1, 2, 4),
        ('2023-04-02 12:10:00', 1, 2, 4),
        ('2023-04-03 09:30:00', 2, 1, 1),
        ('2023-04-01 10:15:00', 2, 1, 1),
        ('2023-04-02 17:30:00', 2, 2, 5),
        ('2023-04-03 14:00:00', 3, 1, 1),
        ('2023-04-01 15:45:00', 3, 2, 3),
        ('2023-04-02 13:00:00', 3, 2, 4),
        ('2023-04-03 10:30:00', 3, 2, 4),
        ('2023-04-01 11:00:00', 4, 1, 5),
        ('2023-04-02 08:45:00', 4, 1, 5),
        ('2023-04-03 16:15:00', 4, 2, 4),
        ('2023-04-01 09:30:00', 4, 2, 4)
    ]

    types_query = '''   
    INSERT INTO space_type (name) VALUES ('global');
    INSERT INTO space_type (name) VALUES ('blog');
    INSERT INTO space_type (name) VALUES ('post');
    
    INSERT INTO event_type (name) VALUES ('login');
    INSERT INTO event_type (name) VALUES ('comment');
    INSERT INTO event_type (name) VALUES ('create_post');
    INSERT INTO event_type (name) VALUES ('delete_post');
    INSERT INTO event_type (name) VALUES ('logout');
    '''

    try:
        cursor.executescript(types_query)
        sqlite_connection.commit()

        cursor.executemany('INSERT INTO logs (datetime, user_id, space_type_id, event_type_id) VALUES (?, ?, ?, ?)', logs)
    except sqlite3.Error as error:
        print("Не удалось вставить значения", error)
        return

    sqlite_connection.commit()
    cursor.close()
    sqlite_connection.close()
    print('База событий заполнена значенями')


if __name__ == '__main__':
    main()
