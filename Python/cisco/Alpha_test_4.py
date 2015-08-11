__author__ = 'TIW'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
sys.path.append(r'D:\Git\Python')
from cisco import Alpha_test_2
from cisco import Alpha_test_3


def print_all():
    Alpha_test_3.b(Alpha_test_2.a())


print_all()
