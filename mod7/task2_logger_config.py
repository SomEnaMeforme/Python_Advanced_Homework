import logging.config
import sys
from mod7.task3_log_handler import LogHandlerForCalculator
from mod7.task4_5_dict_config import dict_config

def logger_config(name: str):
    logging.config.dictConfig(dict_config)
    #logging.basicConfig(
        #level=logging.INFO,
        #datefmt='%Y-%m-%d %H:%M:%S',
        #format='%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s',
        #stream=sys.stdout, # для второй задачи
    #)

    #logger = logging.getLogger(name)
    #calc_handler = LogHandlerForCalculator()
    #logger.addHandler(calc_handler)



