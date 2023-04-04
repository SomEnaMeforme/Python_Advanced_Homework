import logging_tree
import logging
import os

def logs_tree():
    logging.getLogger('CalculationLoggerApps').setLevel('DEBUG')
    logging.getLogger("CalculationLoggerUtils").setLevel('DEBUG')
    logging.getLogger()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    logs_file = os.path.join(base_dir, 'logging_tree.txt')
    with open(logs_file, 'w') as logs_tree:
        logs_tree.write(logging_tree.format.build_description())

if __name__ == '__main__':
    logs_tree()