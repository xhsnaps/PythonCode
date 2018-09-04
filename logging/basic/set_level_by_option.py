#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 10:51
# @Author  : xhsnaps

import logging

numeric_level = getattr(logging, loglevel.upper(), None)

if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % loglevel)

logging.basicConfig(level=numeric_level)
