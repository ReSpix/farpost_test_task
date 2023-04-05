create_author_database = '''
CREATE TABLE post ( 
  id INTEGER PRIMARY KEY,
  header TEXT NOT NULL,
  text TEXT NOT NULL,
  author_id INTEGER NOT NULL,
  blog_id INTEGER NOT NULL,
  FOREIGN KEY (author_id) REFERENCES author(id),
  FOREIGN KEY (blog_id) REFERENCES blog(id)
);

CREATE TABLE author (
  id INTEGER PRIMARY KEY,
  login TEXT NOT NULL,
  email TEXT NOT NULL
);

CREATE TABLE blog (
  id INTEGER PRIMARY KEY,
  owner_id INTEGER NOT NULL,
  name TEXT NOT NULL,
  description TEXT NOT NULL,
  FOREIGN KEY (owner_id) REFERENCES author(id)
);
'''

create_events_database = '''
CREATE TABLE logs (
  id INTEGER PRIMARY KEY,
  datetime TEXT NOT NULL,
  user_id INTEGER NOT NULL,
  space_type_id INTEGER NOT NULL,
  event_type_id INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (space_type_id) REFERENCES space_type(id),
  FOREIGN KEY (event_type_id) REFERENCES event_type(id)
);

CREATE TABLE space_type (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE event_type (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL
);

INSERT INTO space_type (name) VALUES ('global');
INSERT INTO space_type (name) VALUES ('blog');
INSERT INTO space_type (name) VALUES ('post');

INSERT INTO event_type (name) VALUES ('login');
INSERT INTO event_type (name) VALUES ('comment');
INSERT INTO event_type (name) VALUES ('create_post');
INSERT INTO event_type (name) VALUES ('delete_post');
INSERT INTO event_type (name) VALUES ('logout');
'''