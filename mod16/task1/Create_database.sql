DROP TABLE IF EXISTS actors;
DROP TABLE IF EXISTS movie;
DROP TABLE IF EXISTS director;
DROP TABLE IF EXISTS movie_cast;
DROP TABLE IF EXISTS oscar_awarded;
DROP TABLE IF EXISTS movie_direction;


CREATE TABLE actors (
    act_id INTEGER NOT NULL PRIMARY KEY,
    act_first_name VARCHAR(50),
    act_last_name VARCHAR(50),
    act_gender VARCHAR(1)
);


CREATE TABLE movie (
    mov_id INTEGER NOT NULL PRIMARY KEY,
    mov_title VARCHAR(50)
);




CREATE TABLE director (
    dir_id INTEGER NOT NULL PRIMARY KEY,
    dir_first_name VARCHAR(50),
    dir_last_name VARCHAR(50)
);



CREATE TABLE movie_cast (
    act_id INTEGER REFERENCES actors(act_id) ON DELETE CASCADE,
    mov_id INTEGER REFERENCES movie(mov_id) ON DELETE CASCADE,
    role VARCHAR(50)
);



CREATE TABLE oscar_awarded
(
    award_id INTEGER NOT NULL PRIMARY KEY,
    mov_id INTEGER REFERENCES movie(mov_id) ON DELETE CASCADE
);


CREATE TABLE movie_direction (
    dir_id INTEGER REFERENCES director(dir_id) ON DELETE CASCADE,
    mov_id INTEGER REFERENCES movie(mov_id) ON DELETE CASCADE
);

PRAGMA foreign_keys = ON