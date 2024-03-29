'''
Created on Feb 4, 2019

@author: Andrea
'''
def _computeSum(b, SUM):
    '''
    Compute the paid amount with the current candidate
    '''
    amount = 0
    for coin in b:
        nrCoins = (SUM - amount) // coin
        # If this is a candidate solution,
        # we need to use at least 1 coin
        if nrCoins == 0:
            nrCoins = 1
        amount += nrCoins * coin
    return amount

def selectMostPromising(c):
    '''
    Select the largest coin from the remaining
    input:
        c - candidate coins
    Return the largest coin
    '''
    return max(c)

def acceptable(b, SUM):
    '''
    Verify if a candidate solution is valid (we are not over amount)
    '''
    amount = _computeSum(b, SUM)
    return amount <= SUM

def solution(b, SUM):
    '''
    Verify if a candidate solution is an actual solution
    (we are at the required amount)
    '''
    amount = _computeSum(b, SUM)
    return amount == SUM

def buildSolutionString(b, SUM):
    '''
    Pretty print the solution
    '''
    solStr = ''
    amount = 0
    for coin in b:
        nrCoins = (SUM - amount) // coin
        solStr += str(nrCoins) + '*' + str(coin)
        amount += nrCoins * coin
        if SUM - amount > 0:
            solStr += " + " 
    return solStr

def greedy(c, SUM):
    '''
    Main function
    '''
    # The empty set is the candidate solution
    b = [] 
    while not solution(b, SUM) and c != []:
        # Select best candidate (local optimum)
        candidate = selectMostPromising(c)
        c.remove(candidate)
        # If the candidate is acceptable, add it
        if acceptable(b + [candidate], SUM):
            b.append(candidate)
    if solution(b, SUM):
        return buildSolutionString(b, SUM)

'''
    Let's see how it works
'''
for amount in range(1, 55):
    print('Amount ' + str(amount) + "=" + greedy([1, 5, 10], amount))
    
    
