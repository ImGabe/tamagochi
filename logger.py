import logging

logging.basicConfig(filename='tamagochi_logs.log',
                    level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(message)s', 
                    datefmt='%m/%d/%Y %I:%M:%S')


def log_info(x):
    return logging.info(x)

def log_debug(x):
    return logging.debug(x)

def log_error(x):
    return logging.error(x)

def log_warning(x):
    return logging.warning(x)

def log_critical(x):
    return logging.critical(x)
