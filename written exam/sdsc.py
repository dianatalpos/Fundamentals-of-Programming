'''
Created on Feb 4, 2019

@author: Andrea
'''
a = lambda x: [x+1]
b = a(1)
c = lambda x: x + b
d = c([1])
a = 1
b = 3
print (a, b, c(4), d[1])


print(6/3)
print(7/3)
print(7//3)