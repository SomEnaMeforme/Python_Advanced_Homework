import logging
import random
import threading
import time

TOTAL_TICKETS = 10
SEATS_COUNT = 50
SELLER_COUNT = 4

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Director(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore):
        global SEATS_COUNT
        global TOTAL_TICKETS
        super().__init__()
        self.sem = semaphore
        self.can_be_printed_tickets = SEATS_COUNT - TOTAL_TICKETS
        logger.info('Director started work')

    def run(self):
        global TOTAL_TICKETS
        global SELLER_COUNT
        is_running = True
        while is_running:
            self.random_sleep()
            with self.sem:
                if TOTAL_TICKETS - SELLER_COUNT >= 1:
                    continue
                if self.can_be_printed_tickets <= 0:
                    logger.warning(f'There are no seats')
                    break
                new_tickets = 6 if self.can_be_printed_tickets >= 6 else self.can_be_printed_tickets
                TOTAL_TICKETS += new_tickets
                self.can_be_printed_tickets -= new_tickets
                logger.info(f'{self.getName()} printed tickets;  {TOTAL_TICKETS} - total tickets, printed {new_tickets}, {self.can_be_printed_tickets} seats left')

    def random_sleep(self):
        time.sleep(random.randint(0, 1))

class Seller(threading.Thread):

    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.tickets_sold = 0
        logger.info('Seller started work')

    def run(self):
        global TOTAL_TICKETS
        is_running = True
        while is_running:
            self.random_sleep()
            with self.sem:
                if TOTAL_TICKETS <= 0:
                    break
                self.tickets_sold += 1
                TOTAL_TICKETS -= 1
                logger.info(f'{self.getName()} sold one;  {TOTAL_TICKETS} left')

        logger.info(f'Seller {self.getName()} sold {self.tickets_sold} tickets')

    def random_sleep(self):
        time.sleep(random.randint(0, 1))

def main():
    semaphore = threading.Semaphore()
    director = Director(semaphore)
    sellers = []
    for _ in range(4):
        seller = Seller(semaphore)
        seller.start()
        sellers.append(seller)
    director.start()
    for seller in sellers:
        seller.join()
    director.join()
if __name__ == '__main__':
    main()