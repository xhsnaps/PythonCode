#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 11:01
# @Author  : xhsnaps
import logging
import mylib


def main():
    logging.basicConfig(filename="app.log", level=logging.INFO)
    logging.info("Start!")
    mylib.do_something()
    logging.info("Finished!")


if __name__ == '__main__':
    main()
