'''
Created on Jan 14, 2019

@author: Andrea
'''


def consistent(permutation):
    ones = 0
    for i in permutation:
        if i == 1:
            ones += 1
        if ones == 3:
            return False
    if len(permutation) == 4 and permutation[-1] == "X":
        return False
    return True


def is_valid(list):
    '''
    the last element can't be "X"
    max number of 1's must be 2
    '''
    if list[-1] == "X":
        return False
    ones = 0
    for score in list:
        if score == 1:
            ones += 1
        if ones == 3:
            return False
    
    if list[-1] == "X":
        return False
    return True


def back(scores, permutation, l, k):
    '''
    l = the length of the permutation  
    k = the current step
    '''
    if k == l:
        if is_valid(permutation) == True:
            print(permutation)
    else:
        for i in scores:
            permutation[k] = i
            if consistent(permutation):
                back(scores, permutation, l, k+1)

def run():
    scores = [1, "X", 2]
    perm = [0]*4
    l = 4
    k = 0
    back(scores, perm, l, k)


def test_is_valid():
    
    lst = [1,1,1,"X"]
    
    assert is_valid(lst) == False
    
    lst  = [1,1,1,2]
    assert is_valid(lst) == False
    
    lst = [2,1,1,'X']

    assert is_valid(lst) == False
    
    lst = [2,2,"X", 1]
    assert is_valid(lst) == True
    

def test_consistent():
    
    lst = [1,1,1]
    assert consistent(lst) == False
    lst = [1,1]
    assert consistent(lst) == True
    
    lst = [1,2,1,"X"]
    assert consistent(lst) == False


test_is_valid()
test_consistent()    
    
run()    
    
    