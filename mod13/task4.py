import sqlite3

def ivan_sovin_the_most_effective(cursor: sqlite3.Cursor, name: str) -> None:
    if name == 'Иван Совин':
        return None
    cursor.execute(f"SELECT salary FROM table_effective_manager WHERE (name='Иван Совин')")
    manager_salary = int(cursor.fetchone()[0])
    cursor.execute(f"SELECT salary FROM table_effective_manager WHERE (name='{name}')")
    worker_salary = int(cursor.fetchone()[0])
    worker_salary = int(worker_salary) + int(worker_salary) * 0.1
    if manager_salary <= worker_salary:
        cursor.execute(f"DElETE FROM table_effective_manager WHERE (name='{name}') ")
    else:
        cursor.execute(f"UPDATE table_effective_manager SET salary='{worker_salary}' WHERE name='{name}'")

if __name__ == "__main__":
    with sqlite3.connect('hw.db') as connection:
        ivan_sovin_the_most_effective(connection.cursor(), "Петров М.Э.")