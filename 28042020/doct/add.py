#!/usr/bin/env/ python3
'''
'''

def mulf(*vars):
	'''Returns vars[0] * vars[1] * ...
>>> mulf(2)
2
>>> mulf(2,3,4,5)
120
>>> mulf()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/chay-chitsd/prac/28042020/doct/add.py", line 12, in mulf
    v = vars[0]
IndexError: tuple index out of range
>>> mulf(2,10,"A")
'AAAAAAAAAAAAAAAAAAAA'
'''
	v = vars[0]
	for i in vars[1:]:
		v *= i
	return v
