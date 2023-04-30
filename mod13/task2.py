import sqlite3
import csv


def check_if_vaccine_has_spoiled(cursor: sqlite3.Cursor, wrong_fees_file: str) -> None:
    file = open(wrong_fees_file, "r")
    reader = csv.reader(file)
    for idx, line in enumerate(reader):
        if idx == 0:
            continue
        cursor.execute(f"DElETE FROM table_fees WHERE (truck_number='{line[0]}') AND (timestamp='{line[1]}') ")

if __name__ == "__main__":
    with sqlite3.connect('hw.db') as connection:
        check_if_vaccine_has_spoiled(connection.cursor(), "wrong_fees.csv")