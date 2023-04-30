import random as rnd
import sqlite3


def generate_test_data(cursor: sqlite3.Cursor, number_of_groups: int) -> None:
    cursor.execute("DELETE FROM 'uefa_commands'")
    cursor.execute("DELETE FROM 'uefa_draw'")

    countries = ['Россия', 'Германия', 'Испания', 'Франция', 'Италия', 'Англия']
    levels = ['сильная', 'средняя', 'средняя', 'слабая']
    group_number = 0
    count_command_in_group = 4
    for i in range(number_of_groups * count_command_in_group):
        if i % count_command_in_group == 0:
            rnd.shuffle(levels)
            group_number += 1

        cursor.execute(
            "INSERT INTO uefa_commands (command_number, command_name, command_country, command_level) VALUES (?,?,?,?)",
            (i + 1, 'команда ' + str(i + 1), rnd.choice(countries), levels[i % count_command_in_group]))

        cursor.execute(f"INSERT INTO uefa_draw (id, command_number, group_number) VALUES (?,?,?)",
                       (i, i + 1, f'группа {group_number}'))

if __name__ == "__main__":
    with sqlite3.connect('hw.db') as connection:
        generate_test_data(connection.cursor(), 6)