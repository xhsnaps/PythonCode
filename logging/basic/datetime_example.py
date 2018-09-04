#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 11:18
# @Author  : xhsnaps
import logging


# logging.basicConfig(format='%(asctime)s %(message)s')
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning("is when this event was logged")