from datetime import datetime, timedelta

from session_and_base import Base, session, engine
from flask import Flask, jsonify, request
from database_descryption import Book, ReceivingBook

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


if __name__ == "__main__":
    app.run(debug=True)