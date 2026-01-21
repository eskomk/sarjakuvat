CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

create TABLE comics (
  id integer primary key,
  name TEXT unique,
  description TEXT,
  user_id integer references users
);

create table comic_images (
  id integer primary key,
  image blob,
  description TEXT,
  comic_id integer references comics
);

create table comic_types (
  id integer primary key,
  type TEXT unique,
  description text,
  comic_id integer references comics
);

create table comic_stars (
  id integer primary key,
  stars integer,
  description text,
  user_id integer references users,
  comic_id integer references comics
);

-- Ref: comics.user_id > users.id
-- Ref: comic_images.comic_id > comics.id
-- Ref: comic_type.comic_id > comics.id
-- Ref: comic_star.comic_id > comics.id
-- Ref: comic_star.user_id > users.id
