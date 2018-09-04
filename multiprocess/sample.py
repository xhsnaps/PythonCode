#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 11:55
# @Author  : xhsnaps

from multiprocessing import Process
import os


def run_proc(name):
    print("Run child process %s (%s)..." % (name, os.getpid()))


if __name__ == '__main__':
    print("Parent process %s." % os.getpid())
    p = Process(target=run_proc, args=('test', ))
    print("Child process will start!")
    p.start()
    print("Child process will join!")
    p.join()
    print("Child process end!")