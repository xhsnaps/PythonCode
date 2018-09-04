#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 11:18
# @Author  : xhsnaps

import logging
import threading
import time


def worker(arg):
    while not arg['stop']:
        logging.debug("Hi from myfunc")
        time.sleep(1)


def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(relativeCreated)6d %(threadName)s %(message)s')
    info = {'stop' : False}
    thread = threading.Thread(target=worker, args=(info,))
    thread.start()

    while True:
        try:
            logging.debug("Hello from main")
            time.sleep(0.75)
        except KeyboardInterrupt:
            info['stop'] = True
    thread.join()

if __name__ == '__main__':
    main()