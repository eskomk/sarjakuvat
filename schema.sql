CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

create TABLE comics (
  id integer primary key,
  title TEXT unique,
  description TEXT,
  user_id integer,
  type_id integer references comic_types,
  foreign key (user_id) references users(id) on delete cascade
);

create table comic_images (
  id integer primary key,
  image blob,
  description TEXT,
  comic_id integer references comics
);

create table comic_types (
  id integer primary key,
  comic_type TEXT unique
);

create table comic_stars (
  -- id integer autoincrement,
  stars integer CHECK(stars >= 1 AND stars <= 5),
  description text,
  user_id integer,
  comic_id integer,
  primary key (user_id, comic_id),
  foreign key (user_id) references users ON DELETE CASCADE,
  foreign key (comic_id) references comics ON DELETE CASCADE
);

-- Ref: comics.user_id > users.id
-- Ref: comic_images.comic_id > comics.id
-- Ref: comic_type.comic_id > comics.id
-- Ref: comic_star.comic_id > comics.id
-- Ref: comic_star.user_id > users.id
