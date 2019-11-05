'''
Created on Feb 4, 2019

@author: Andrea
'''
def max_subarray(X):
    '''
    We traverse the array once. For each index i  in the array, we calculate the maximum subarray sum ending at that index. 
    If that sum is larger than the one previously recorded, we remember it (in the max_so_far variable)
    '''
    max_ending_here = max_so_far = X[0]
    for x in X[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


data = [-2, -5, 6, -2, -3, 1, 5, -6]
print(max_subarray(data))
    