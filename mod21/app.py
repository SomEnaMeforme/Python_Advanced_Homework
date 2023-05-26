from datetime import datetime, timedelta
from sqlalchemy import func
from session_and_base import Base, session, engine, Session
from flask import Flask, jsonify, request
from database_descryption import Book, ReceivingBook, Student
import csv

app = Flask(__name__)


@app.before_request
def before_request_func() -> None:
    Base.metadata.create_all(engine)


#получить все книги в библиотеке (GET)
@app.route("/all_books", methods=["GET"])
def get_all_books():
    return jsonify(books_list=Book.get_books()), 200


#получить список должников, которые держат книги у себя более 14 дней (GET)
@app.route("/debtors", methods=["GET"])
def get_student_debtors():
    debtors = ReceivingBook.get_debtors(timedelta(days=14))
    if debtors is None or len(debtors) == 0:
        return 'Нет должников', 201
    return jsonify(debtors_list=debtors), 200


#выдать книгу студенту (POST — входные параметры ID книги и ID студента)
@app.route("/give_book_to_student", methods=["POST"])
def give_book_to_student():
    book_id = request.form.get('book_id', type=int)
    student_id = request.form.get('student_id', type=int)
    record = ReceivingBook(book_id=book_id,
                           student_id=student_id,
                           date_of_issue=datetime.now())
    session.add(record)
    session.commit()
    return f"Студент с идентификационным номером {student_id} успешно получил книгу с идентификационным номером {book_id}", 201


#сдать книгу в библиотеку (POST — входные параметры ID книги и ID студента, если такой связки нет, выдать ошибку)
@app.route("/return_book_from_student", methods=["POST"])
def return_book_from_student():
    book_id = request.form.get('book_id', type=int)
    student_id = request.form.get('student_id', type=int)
    record = session.query(ReceivingBook).filter(ReceivingBook.book_id == book_id,
                                                 ReceivingBook.student_id == student_id).one_or_none()
    if record is None:
        return f'К сожелению книга с номером {book_id} и студент с номером {student_id} не найдены', 400
    record.date_of_return = datetime.now()
    session.add(record)
    session.commit()
    return f"Студент с идентификационным номером {student_id} успешно сдал книгу с идентификационным номером {book_id}", 201


#Создайте роут, с помощью которого можно найти книгу по названию. На вход передаётся строка, по которой будет выполнен поиск.
# Поиск должен выдавать книги, в названии которых содержится ключевая строка.
@app.route("/book/<title>", methods=["GET"])
def get_specific_book(title):
    books_list = Book.get_books_with_specific_title(title)
    if books_list is None or len(books_list) == 0:
        return "Книг с таким названием нет", 400
    return jsonify(books_list=books_list), 200


@app.route('/avg_books_taken_students_in_current_month', methods=['GET'])
def book_of_the_month():
    first_day_of_month = datetime.now().today().replace(day=1)
    book_count = session.query(func.count(ReceivingBook.book_id)) \
        .filter(ReceivingBook.date_of_issue >= first_day_of_month)\
        .scalar()
    students_count = session.query(func.count(Student.id)).scalar()
    avg_book_month_count = round(book_count / students_count, 2)
    return f'Среднее количество книг на одного студента в этом месяце {avg_book_month_count}', 200


@app.route('/most_popular_book', methods=['GET'])
def most_popular_book_for_good_students():
    book_id = session.query(func.count(ReceivingBook.book_id)) \
        .filter(ReceivingBook.student_id == Student.id, Student.average_score >= 4.0) \
        .group_by(ReceivingBook.book_id) \
        .order_by(func.count(ReceivingBook.book_id).desc()) \
        .limit(1) \
        .all()
    book = session.query(Book).filter(Book.id == book_id[0][0]).all()
    return jsonify(the_most_popular_book=book[0].to_json()), 200

@app.route('/books_by_author/<int:author_id>')
def books_by_author(author_id):
    available_books = session.query(Book).filter(Book.author_id == author_id, Book.id == ReceivingBook.book_id, ReceivingBook.date_of_return == None).all()
    books_list = [book.to_json() for book in available_books]
    return jsonify(available_books_list=books_list), 200


def is_student_with_scholarship(student):
    return student['scholarship'].lower() == 'true'

@app.route('/most_reading_students', methods=['GET'])
def most_reading_students():
    current_year_start = datetime(datetime.now().year, 1, 1, 0, 0, 0, 0)
    students = session.query(Student).filter(ReceivingBook.student_id == Student.id, ReceivingBook.date_of_issue >= current_year_start)\
        .group_by(ReceivingBook.student_id)\
        .order_by(func.count(ReceivingBook.book_id).desc())\
        .limit(10)\
        .all()
    students_list = [student.to_json() for student in students]
    return jsonify(most_reading_students=students_list), 200

@app.route('/load_csv_data_for_students', methods=['POST'])
def most_reading_students():
    file = request.files.get('students')
    if file:
        file.save('students.csv')
        with open('students.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            students = []
            for student in reader:
                student['scholarship'] = is_student_with_scholarship(student)
                students.append(student)
                session.bulk_insert_mappings(Student, students)
                session.commit()
            return 'Студенты были добавлены', 200
    return 'Добавить студентов не удалось - не найден файл', 404



@app.route('/books_not_readed_by_student/<int:student_id>')
def books_not_readed_by_student(student_id):
    books_readed_by_student = session.query(ReceivingBook.book_id).distinct().filter(ReceivingBook.book_id == Book.id, ReceivingBook.student_id == student_id).all()
    authors_id = session.query(Book.author_id).distinct().filter(ReceivingBook.book_id == Book.id, ReceivingBook.student_id == student_id).all()
    authors_id = [item[0] for item in authors_id]

    books_authors = session.query(Book.id).filter(Book.author_id .in_(authors_id)).all()
    not_readed_books = [book_id for book_id in books_authors if book_id not in books_readed_by_student]
    indexes = [books_authors.index(element) for element in not_readed_books]

    books_by_authors = session.query(Book).filter(Book.author_id.in_(authors_id)).all()
    books = [books_by_authors[i].to_json() for i in indexes]
    return jsonify(recomended_books_list=books), 200


if __name__ == "__main__":
    app.run(debug=True)