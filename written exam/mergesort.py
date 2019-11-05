'''
Created on Feb 13, 2019

@author: Andrea
'''
def qsort(l):
    if l == []:
        return []
    else:
        pivot = l[0]
        lesser = qsort([x for x in l[1:] if x<pivot])
        greater = qsort([x for x in l[1:] if x>=pivot])
        return lesser +[pivot]+greater 

l=[7,0,17,5,9,24]
print(qsort(l))