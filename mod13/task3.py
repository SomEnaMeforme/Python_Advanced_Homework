import sqlite3

def log_bird(cursor: sqlite3.Cursor, bird_name: str, date_time: str) -> None:
  cursor.execute(f"INSERT INTO 'birds' (bird_name, date_time) VALUES('{bird_name}','{date_time}');")


def check_if_such_bird_already_seen(cursor: sqlite3.Cursor, bird_name: str) -> bool:
    cursor.execute(f"SELECT COUNT(*) FROM birds WHERE (bird_name='{bird_name}')")
    return cursor.fetchone()[0] > 0


if __name__ == "__main__":
    with sqlite3.connect('birds.db') as connection:
        print(check_if_such_bird_already_seen(connection.cursor(), "неизвестная птица"))
        log_bird(connection.cursor(), "неизвестная птица", "08.04.2005")
        print(check_if_such_bird_already_seen(connection.cursor(), "воробей"))
        print(check_if_such_bird_already_seen(connection.cursor(), "неизвестная птица"))