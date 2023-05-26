from datetime import datetime
from sqlalchemy import Column, Integer, Date, Text, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from typing import Dict, Any, Tuple, List
from session_and_base import Base, session
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship, backref


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(Date, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    author = relationship("Author", backref=backref("books",
                                                    cascade="all, "
                                                            "delete-orphan",
                                                    lazy='joined'))
    students = association_proxy('book', 'ReceivingBook')

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def get_books(cls):
        books = session.query(cls).all()
        return [book.to_json() for book in books]

    @classmethod
    def get_books_with_specific_title(cls, title):
        books = session.query(cls).filter(cls.name.like(f'%{title}%'))
        return [book.to_json() for book in books]


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    surname = Column(Text, nullable=False)
    phone = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    books = association_proxy('student', 'ReceivingBook')

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def get_students_with_scholarship(cls) -> Tuple[Any, int]:
        try:
            return session.query(cls).filter(cls.scholarship == True), 200
        except NoResultFound:
            return 'К сожалению, на данный момент студентов, проживающих в общежитии, нет', 400

    @classmethod
    def get_students_with_specific_score(cls, score: float) -> Tuple[Any, int]:
        try:
            return session.query(cls).filter(cls.average_score >= score), 200
        except NoResultFound:
            return f'Студенты, с количеством баллов, превышающих {score} не найдены ', 400


class ReceivingBook(Base):
    __tablename__ = 'receiving_books'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    date_of_issue = Column(DateTime, nullable=False)
    date_of_return = Column(DateTime)

    student = association_proxy("books", "Student")
    book = association_proxy("students", "Book")

    @hybrid_property
    def count_date_with_book(self):
        return \
            self.date_of_return - self.date_of_issue \
            if self.date_of_return \
            else datetime.now() - self.date_of_issue

    @hybrid_method
    def is_debtor(self, delta):
        return self.date_of_issue + delta < datetime.now()

    @classmethod
    def get_debtors(cls, delta):
        debtors = session.query(Student).filter(cls.is_debtor(delta))
        if debtors is None:
            return None
        return [debtor.to_json() for debtor in debtors]