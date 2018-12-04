#! /usr/bin/env python
#-*- coding:utf-8 -*-
import time
def foo():
    sum = 0
    for i in range(100):
        time.sleep(0.1)
        sum += i
    return sum

import cProfile
cProfile.run("foo()")