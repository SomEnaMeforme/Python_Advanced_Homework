import sqlite3


if __name__ == "__main__":
    with sqlite3.connect("../hw_3_database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT  COUNT(*) FROM  'table_1'")
        answer_11 = cursor.fetchone()
        cursor.execute("SELECT  COUNT(*) FROM  'table_2'")
        answer_12 = cursor.fetchone()
        cursor.execute("SELECT  COUNT(*) FROM  'table_3'")
        answer_13 = cursor.fetchone()
        cursor.execute("SELECT  COUNT(DISTINCT value) FROM  'table_1'")
        answer_2 = cursor.fetchone()
        cursor.execute("SELECT COUNT(*) FROM (SELECT value FROM 'table_1' INTERSECT SELECT value FROM 'table_1')")
        answer_3 = cursor.fetchone()
        cursor.execute(
            "SELECT COUNT(*) FROM (SELECT value FROM 'table_3' INTERSECT SELECT value FROM (SELECT value FROM 'table_1' INTERSECT SELECT value FROM 'table_1'))"
        )
        answer_4 = cursor.fetchone()
    print(f"Сколько записей (строк) хранится в каждой таблице? - {answer_11[0]}, {answer_12[0]}, {answer_13[0]}")
    print(f"Сколько в таблице table_1 уникальных записей? - {answer_2[0]}")
    print(f"Как много записей из таблицы table_1 встречается в table_2? - {answer_3[0]}")
    print(f"Как много записей из таблицы table_1 встречается в table_2? - {answer_4[0]}")


