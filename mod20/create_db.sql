CREATE TABLE IF not EXISTS books (
id integer PRIMARY KEY,
name text NOT NULL,
count int default 1,
release_date date not null,
author_id int not null)


CREATE TABLE IF not EXISTS authors (
id integer PRIMARY KEY,
name text NOT NULL,
surname text NOT NULL
)


CREATE TABLE IF not EXISTS students (
id integer PRIMARY KEY,
name text NOT NULL,
surname text NOT NULL,
phone text NOT NULL,
email text NOT NULL,
average_score float NOT NULL,
scholarship boolean NOT NULL
)


CREATE TABLE IF not EXISTS receiving_books (

id integer PRIMARY KEY,

book_id int NOT NULL,

student_id int NOT NULL,

date_of_issue datetime not null,

date_of_return datetime

)

