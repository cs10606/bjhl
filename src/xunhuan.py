# -*- coding:utf-8 -*-
import sys

i = [1, 2, 3, 4, 5, 6, 7, 8]
for a in i:
    print a

j = ['a', 'b', 'c']
m = range(len(j))
print m

print 'this is a good'
s = 'abc'
print sys.getsizeof(s)

"""
求100内所有奇数的平方和
"""
l = xrange(1,100,2)
for i in xrange(len(l)):
    print l[i]
    nl = [i * i for i in range(len(l))]
    print nl[i]