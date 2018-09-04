#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 13:12
# @Author  : xhsnaps

log_dir = ".//log//"

log_configs = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
        'app1': {
            'class': 'logging.FileHandler',
            'filename': log_dir +'app1.log',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
        'app2': {
            'class': 'logging.FileHandler',
            'filename': log_dir + 'app2.log',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
        'app3': {
            'class': 'logging.FileHandler',
            'filename': log_dir + 'app3.log',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
        'lib1': {
            'class': 'logging.FileHandler',
            'filename': log_dir + 'lib1.log',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
    },
    'loggers':{
        'root': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'app1' : {
            'handlers': ['app1','console'],
            'level': "DEBUG",
        },
        'app2': {
            'handlers': ['app2', 'console'],
            'level': "DEBUG",
        },
        'app3': {
            'handlers': ['app3', 'console'],
            'level': "DEBUG",
        },
        'lib1': {
            'handlers': ['lib1', 'console'],
            'level': "DEBUG",
        },
    }
}