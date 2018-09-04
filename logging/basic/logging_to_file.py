#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(filename='example.log', level=logging.DEBUG)
# filemode='w' 每次调用重新开始写文件
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
