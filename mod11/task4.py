import queue
from queue import PriorityQueue
import threading
from threading import Lock
import random as rnd
import logging
import time




NUMB = 2
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def task():
    global NUMB
    NUMB *= 2
    logger.info(f'Current value: {NUMB}')


class Producer(threading.Thread):
    def __init__(self, queue, lock):
        super().__init__()
        self.tasks = queue
        self.lock = lock
        logger.info(f'{self.name} running')

    def run(self):
        with self.lock:
            for _ in range(20):
                self.tasks.put((rnd.randint(1, 100), task))




class Consumer(threading.Thread):

    def __init__(self, queue, lock):
        super().__init__()
        self.tasks = queue
        self.lock = lock
        logger.info(f'{self.name} running')


    def run(self):
        while True:
            with self.lock:
                if self.tasks.empty():
                    break
                priority, task = self.tasks.get()
                logger.info(f'running Task(priority={priority})')
                task()
                self.random_sleep()

    def random_sleep(self):
        time.sleep(rnd.randint(0, 1))


def main():
    lock = Lock()
    queue = PriorityQueue()
    producer = Producer(queue, lock)
    producer.start()
    consumer = Consumer(queue, lock)
    consumer.start()
    producer.join()
    consumer.join()

if __name__ == '__main__':
    main()