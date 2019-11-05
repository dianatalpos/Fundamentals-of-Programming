'''
Created on Feb 3, 2019

@author: Andrea
'''

def insertionSort(list):
    for i in range (1, len(list)):
        index = i-1
        elem = list[i]
        while index >= 0 and elem < list[index]:
            list[index+1] = list[index]
            index -= 1
            
        list[index + 1] = elem 
        
list = [0, 5, 2, 10, 3, 9]
insertionSort(list)
print (list)