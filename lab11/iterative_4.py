'''
Created on Jan 14, 2019

@author: Andrea
'''


def solution(x):
    return len(x) == 4

def solution_print(x):
    print(x)

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
            
def next_score(score):
    if score == 0:
        return 1
    if score == 1:
        return "X"
    if score == "X":
        return 2
    return None


def back_it():

    list = [0]
    while len(list) > 0:
        chosen = False
        while not chosen and next_score(list[-1]) != None:
            list[len(list) - 1] = next_score( list[len(list)-1])
            chosen = consistent(list)
        if chosen:
            if solution(list):
                solution_print(list)
            else:
                list.append(0)
        else:
            list = list[:-1]
            
            
def run():
    back_it()
    
run()