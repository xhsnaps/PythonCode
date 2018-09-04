#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 13:10
# @Author  : xhsnaps

from config import log_configs
import logging, logging.config


logging.config.dictConfig(log_configs)

logger = logging.getLogger("app1")

logger.info("run app1")

from lib1 import do_sth_lib1

do_sth_lib1()