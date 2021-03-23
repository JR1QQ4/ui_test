#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging

from demo_a.utils.get_path import *

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
all_log_path = logs_path + "/all.log"
error_log_path = logs_path + "/error.log"

fh_all = logging.FileHandler(all_log_path)
fh_all.setLevel(logging.DEBUG)

fh_error = logging.FileHandler(error_log_path)
fh_error.setLevel(logging.ERROR)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - %(filename)s - %(module)s(%(lineno)d) : %(message)s")
ch.setFormatter(formatter)
fh_all.setFormatter(formatter)
fh_error.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh_all)
logger.addHandler(fh_error)

# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')
