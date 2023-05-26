import requests
import time
import threading
import logging
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from multiprocessing import Pool, cpu_count
from multiprocessing.pool import ThreadPool


engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)


def clear_db():
    session.query(Peoples).delete()


class Peoples(Base):
    __tablename__ = 'peoples'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birth_year = Column(String, nullable=False)
    gender = Column(String, nullable=False)


def get_person_from_response(id: int):
    url = f'https://swapi.dev/api/people/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        data = dict(response.json())
        person = Peoples(id=id, name=data['name'], birth_year=data["birth_year"], gender=data["gender"])
        session.add(person)


def pool():
    start = time.time()
    with Pool(processes=cpu_count()) as pool:
        _ = pool.map(get_person_from_response, [id for id in range(1, 21)])
    logger.info(f"Time from start load persons: {time.time()-start}. One thread")


def thread_pool():
    start = time.time()
    with ThreadPool(processes=cpu_count()) as thread:
        thread.map_async(get_person_from_response, [id for id in range(1, 21)])
    logger.info(f"Time from start load persons: {time.time() - start}. Many threads")

if __name__=="__main__":
    Base.metadata.create_all(engine)
    clear_db()
    pool()
    clear_db()
    thread_pool()



