#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 16:17
# @Author  : xhsnaps
from multiprocessing import Process, Queue
import os, time, random


def write(q):
    print("Process to write: %s" % os.getpid())

    for value in ['A', 'B', 'C']:
        print("Put %s to queue..." % value)
        q.put(value)
        time.sleep(random.random()*10)


def read(q):
    print("Process to read: %s" % os.getpid())

    while True:
        value = q.get(True)
        print("Get %s from queue." % value)


if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))

    pw.start()
    pr.start()

    pw.join()
    pr.terminate()
