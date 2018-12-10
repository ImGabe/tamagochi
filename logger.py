import logging

logging.basicConfig(filename='example.log',
                    level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(message)s', 
                    datefmt='%m/%d/%Y %I:%M:%S')

def log_info(x):
    return logging.info(x)