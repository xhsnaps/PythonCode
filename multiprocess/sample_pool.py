#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 14:14
# @Author  : xhsnaps

from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print("Run task %s (%s)..." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()
    print("Task %s runs %0.2f seconds." % (name, (end-start)))


if __name__ == "__main__":
    print("Parent process %s." % os.getpid())
    p = Pool(3)

    for i in range(5):
        p.apply_async(long_time_task, args=(i, ))
    print("Waiting for all subprocesses done...")
    p.close()
    print("Waiting for all subprocesses join...")
    p.join()
    print("All subprocesses done.")