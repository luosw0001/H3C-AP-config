__author__ = 'TIW'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test(*parms):
	print('参数长度是：', len(parms))
	print('第二个参数是：', parms[1])

test(1, '小甲鱼', 3.14, 5, 6, 7, 8)