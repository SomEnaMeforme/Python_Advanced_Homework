import sqlite3


if __name__ == "__main__":
    with sqlite3.connect("./hw_4_database.db") as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT AVG(salary) FROM 'salaries'")
        mid_salary = cursor.fetchone()

        cursor.execute("SELECT COUNT(*) FROM salaries WHERE salary < 5000")
        poor = cursor.fetchone()


        cursor.execute('SELECT salary FROM salaries ORDER BY salary')
        result = cursor.fetchall()
        median = result[(len(result)+1) // 2][0]

        cursor.execute("SELECT SUM(salary) FROM salaries")
        total_sum =cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM salaries")
        total_count = cursor.fetchone()[0]
        cursor.execute(f"SELECT SUM(salary) FROM (SELECT*FROM salaries ORDER BY salary DESC LIMIT 0.1 * {total_count})")
        T = cursor.fetchone()[0]
        coef = round(T/(total_sum - T)*100, 2)
    print(f"Средняя зарплата - {mid_salary[0]}, медиана - {median}, количество бедняков - {poor[0]}, F - {coef}")




