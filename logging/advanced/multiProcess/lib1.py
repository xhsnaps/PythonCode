#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 9:56
# @Author  : xhsnaps
from config import log_configs
import logging, logging.config


logging.config.dictConfig(log_configs)

logger = logging.getLogger("lib1")


def do_sth_lib1():
    logger.info("do something in lib1")