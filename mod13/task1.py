import sqlite3

def check_if_vaccine_has_spoiled(c: sqlite3.Cursor, truck_number: str,) -> bool:
    c.execute(f"SELECT COUNT(*) FROM table_truck_with_vaccine WHERE (truck_number='{truck_number}') AND (NOT temperature_in_celsius BETWEEN 16 and 20 )  ")
    vaccine = c.fetchone()[0]
    return  vaccine < 3


if __name__ == "__main__":
    with sqlite3.connect('hw.db') as connection:
        print(check_if_vaccine_has_spoiled( connection.cursor(), "к515ва777"))