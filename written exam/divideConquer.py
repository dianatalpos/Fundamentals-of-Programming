'''
Created on Feb 4, 2019

@author: Andrea
'''

 
list = [2, 2, 4, 5, 6, 4, 13, 4, 10]
# sum = 2+4+6+10

def sum(list):
    if len(list) <2 :
        return 0
    if len(list) == 2:
        if list[0] % 2 == 0:
            return list[0]
        else:
            return 0
        
    mid = len(list)//2
    if len(list)%2 == 1:
        list = list + [0]
    if mid%2 == 1:
        s1 = sum(list[:mid-1])  
        s2 = sum(list[mid-1:])
    else:
        s1 = sum(list[:mid])  
        s2 = sum(list[mid:])
   
    return s1+s2


print([2,3,2,1,6,8,9,7,6,4])
print(sum([2,3,2,1,5,8,9,7,6,4]))


print(sum(list))  
print(list)