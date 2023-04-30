import sqlite3
from datetime import datetime
import datetime


def update_work_schedule(cursor):
    hobbies = {
        "футбол": 1,
        "хоккей": 2,
        "шахматы": 3,
        "SUP сёрфинг": 4,
        "бокс": 5,
        "Dota2": 6,
        "шах-бокс": 0
    }

    employees = {}
    for row in cursor.execute("SELECT id, preferable_sport FROM table_friendship_employees"):
        employees[row[0]] = row[1]
    dates = {}
    people = {}
    cursor.execute("SELECT date FROM table_friendship_schedule ORDER BY date")
    date = datetime.strptime(cursor.fetchone()[0], '%Y-%m-%d')
    while len(employees) != 0:
        worker_days = sum(people.values())

        for i in employees:
            if date in dates and len(dates[date]) == 10:
                date += datetime.timedelta(days=1)
                break
            if i in people and people[i] == 10:
                employees.pop(i)
                break

            hobby_weekday = hobbies[employees[i]]

            current_data_weekday = date.weekday()


            if hobby_weekday != current_data_weekday:

               if not(date in dates):
                  dates[date] = [(i, employees[i])]
               else:
                   dates[date].append((i, employees[i]))
               if not(i in people):
                   people[i] = 1
               else:
                   people[i] += 1
            if(i==list(employees.items())[-1][0] and sum(people.values())==worker_days):
                for j in dates:
                    boolka=False
                    if not (i, employees[i]) in dates[j]:
                        for k in dates[j]:
                            if k[1]!=employees[i]:

                                if not (date in dates):
                                    dates[date] = [(k[0], k[1])]
                                else:
                                    dates[date].append((k[0], k[1]))
                                dates[j].append((i, employees[i]))
                                dates[j].remove(k)
                                if not (i in people):
                                    people[i] = 1
                                else:
                                    people[i] += 1
                                boolka=True
                                break
                    if boolka:
                        break
    cursor.execute("DELETE FROM 'table_friendship_schedule'")
    for i in dates:
        for j in dates[i]:
            cursor.execute("INSERT INTO 'table_friendship_schedule' (employee_id, date) VALUES (?, ?) ",
                   (j[0], i.date(),))

if __name__ == "__main__":
    with sqlite3.connect('hw.db') as connection:
        update_work_schedule(connection.cursor())