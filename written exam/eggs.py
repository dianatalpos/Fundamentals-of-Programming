'''
Created on Feb 4, 2019

@author: Andrea
'''
import math
''' 
Function to get minimum number of trails needed in worst # case with n eggs and k floors

input:
    n - Number of eggs remaining
    k - Number of floors

output:
    The number of minimum drops, if following optimal solution
    
    credit - This code is contributed by Bhavya Jain
    http://www.geeksforgeeks.org/dynamic-programming-set-11-egg-dropping-puzzle/
'''
def eggDrop(n, k):
    ''' 
    A 2D table where every eggFloor[i][j] will represent minimum 
    number of trials needed for i eggs and j floors.
    '''
    eggFloor = [[0 for x in range(k + 1)] for x in range(n + 1)]
 
    '''
    We need one trial for one floor and0 trials for 0 floors
    '''
    for i in range(1, n + 1):
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0
 
    '''
    We always need j trials for one egg and j floors.
    '''
    for j in range(1, k + 1):
        eggFloor[1][j] = j
 
    '''
    Fill rest of the entries in table using optimal substructure property
    '''
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            eggFloor[i][j] = math.inf
            for x in range(1, j + 1):
                res = 1 + max(eggFloor[i - 1][x - 1], eggFloor[i][j - x])
                if res < eggFloor[i][j]:
                    eggFloor[i][j] = res
 
    '''
    eggFloor[n][k] holds the result
    '''
    return eggFloor[n][k]

def test_egg_drop():
    n = 2
    k = 100
    print("Minimum number of drops in the worst case with " + str(n) + " eggs and " + str(k) + " floors is " + str(eggDrop(n, k)))

test_egg_drop()