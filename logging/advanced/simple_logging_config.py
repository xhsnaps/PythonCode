#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 11:53
# @Author  : xhsnaps
import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')