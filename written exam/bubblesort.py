'''
Created on Feb 3, 2019

@author: Andrea
'''


def bubbleSort(data):
    done = False
    while not done:
        done = True 
        for i in range(0, len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                done = False
                
                
l = [2, 4, 2, 1, 10, 9, 6 ]
bubbleSort(l)
print(l)