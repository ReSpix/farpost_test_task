create_author_database = '''
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY,
  login TEXT NOT NULL,
  email TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS blog (
  id INTEGER PRIMARY KEY,
  owner_id INTEGER NOT NULL,
  name TEXT NOT NULL,
  description TEXT NOT NULL,
  
  FOREIGN KEY (owner_id) REFERENCES author(id)
);

CREATE TABLE IF NOT EXISTS post ( 
  id INTEGER PRIMARY KEY,
  header TEXT NOT NULL,
  text TEXT NOT NULL,
  author_id INTEGER NOT NULL,
  blog_id INTEGER NOT NULL,
  
  FOREIGN KEY (author_id) REFERENCES author(id),
  FOREIGN KEY (blog_id) REFERENCES blog(id)
);

CREATE TABLE IF NOT EXISTS comment (
  id INTEGER PRIMARY KEY,
  text TEXT NOT NULL,
  user_id INTEGER NOT NULL,
  post_id INTEGER NOT NULL,
  
  FOREIGN KEY (user_id) REFERENCES user(id),
  FOREIGN KEY (post_id) REFERENCES post(id)
);
'''

create_events_database = '''
CREATE TABLE IF NOT EXISTS logs (
  id INTEGER PRIMARY KEY,
  datetime TEXT NOT NULL,
  user_id INTEGER NOT NULL,
  space_type_id INTEGER NOT NULL,
  event_type_id INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (space_type_id) REFERENCES space_type(id),
  FOREIGN KEY (event_type_id) REFERENCES event_type(id)
);

CREATE TABLE IF NOT EXISTS space_type (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS event_type (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL
);
'''

select_event_by_user = '''
SELECT strftime('%Y-%m-%d', datetime) AS 'date',
    SUM(CASE WHEN event_type_id = 1 THEN 1 ELSE 0 END) AS 'logins',
    SUM(CASE WHEN event_type_id = 5 THEN 1 ELSE 0 END) AS 'logouts',
    SUM(CASE WHEN space_type_id = 2 THEN 1 ELSE 0 END) AS 'blog_events'
FROM logs
WHERE user_id = "{}"
GROUP BY strftime('%Y-%m-%d', datetime);
'''

get_user_id_by_login = 'SELECT id FROM users WHERE login = "{}";'

select_comments_info_by_user_id = '''
SELECT
    usr.login as "login",
    p.header AS "header",
    athr.login AS "author",
    COUNT(c.id) AS "amount"
FROM post p
JOIN users athr ON p.author_id = athr.id
JOIN comment c ON p.id = c.post_id
JOIN users usr ON c.user_id = usr.id
WHERE usr.id = {}
GROUP BY p.id;
'''
