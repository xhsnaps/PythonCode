#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 16:27
# @Author  : xhsnaps
import time, threading


def loop():
    print("Thread %s is running..." % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print("thread %s >>> %s" % (threading.current_thread().name, n))
        time.sleep(1)
    print("Thread %s ended." % threading.current_thread().name)


print('Thread %s is running...' % threading.current_thread().name)

t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()

print("Thread %s ended" % threading.current_thread().name)