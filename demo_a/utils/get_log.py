#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import sys

from colorama import Style, Fore

from demo_a.utils.get_path import *


class LevelFilter(logging.Filter):
    def __init__(self, logger, name=''):
        super(LevelFilter, self).__init__()
        self.logger = logger

    def filter(self, record):
        ch = logging.StreamHandler()
        if record.levelno == logging.DEBUG:
            ch.setLevel(logging.DEBUG)
            ch_formatter_debug = logging.Formatter(
                Fore.BLUE + "%(asctime)s-%(filename)s-%(module)s(%(lineno)d)[%(levelname)s]: %(message)s")
            ch.setFormatter(ch_formatter_debug)
            self.logger.addHandler(ch)
            return True
        elif record.levelno == logging.INFO:
            ch.setLevel(logging.INFO)
            ch_formatter_info = logging.Formatter(
                Fore.GREEN + "%(asctime)s-%(filename)s-%(module)s(%(lineno)d)[%(levelname)s]: %(message)s")
            ch.setFormatter(ch_formatter_info)
            self.logger.addHandler(ch)
            return True
        elif record.levelno == logging.WARNING:
            ch.setLevel(logging.WARNING)
            ch_formatter_warning = logging.Formatter(
                Fore.YELLOW + "%(asctime)s-%(filename)s-%(module)s(%(lineno)d)[%(levelname)s]: %(message)s")
            ch.setFormatter(ch_formatter_warning)
            self.logger.addHandler(ch)
            return True
        elif record.levelno == logging.ERROR:
            ch.setLevel(logging.ERROR)
            ch_formatter_error = logging.Formatter(
                Fore.RED + "%(asctime)s-%(filename)s-%(module)s(%(lineno)d)[%(levelname)s]: %(message)s")
            ch.setFormatter(ch_formatter_error)
            self.logger.addHandler(ch)
            return True
        elif record.levelno == logging.CRITICAL:
            ch.setLevel(logging.CRITICAL)
            ch_formatter_critical = logging.Formatter(
                Fore.LIGHTRED_EX + "%(asctime)s-%(filename)s-%(module)s(%(lineno)d)[%(levelname)s]: %(message)s")
            ch.setFormatter(ch_formatter_critical)
            self.logger.addHandler(ch)
            return True


class Log:
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    def __init__(self):
        # create file handler which logs even debug messages
        all_log_path = logs_path + "/all.log"
        error_log_path = logs_path + "/error.log"

        # create console handler with a higher log level
        # self.logger.addFilter(LevelFilter(self.logger))
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch_formatter_debug = logging.Formatter(
            Fore.YELLOW + "%(asctime)s" + Fore.GREEN + " [%(levelname)s]: %(message)s")
        ch.setFormatter(ch_formatter_debug)
        self.logger.addHandler(ch)

        # create formatter and add it to the handlers

        fh_all = logging.FileHandler(all_log_path, encoding="utf-8")
        fh_all.setLevel(logging.DEBUG)
        fh_error = logging.FileHandler(error_log_path, encoding="utf-8")
        fh_error.setLevel(logging.ERROR)

        fh_formatter = logging.Formatter(
            "%(asctime)s - %(filename)s-%(module)s(%(lineno)d) [ %(levelname)s ]: %(message)s")
        fh_all.setFormatter(fh_formatter)
        fh_error.setFormatter(fh_formatter)

        self.logger.addHandler(fh_all)
        self.logger.addHandler(fh_error)

    @classmethod
    def debug(cls, msg):
        cls.logger.debug(str(msg))

    @classmethod
    def info(cls, msg):
        cls.logger.info(str(msg))

    @classmethod
    def warning(cls, msg):
        cls.logger.warning(str(msg))

    @classmethod
    def error(cls, msg):
        cls.logger.error(str(msg))

    @classmethod
    def critical(cls, msg):
        cls.logger.critical(str(msg))

# logger = Log()
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')
