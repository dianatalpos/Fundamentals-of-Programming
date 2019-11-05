'''
Created on Nov 14, 2018

@author: Andrea
'''
from validate import *
from parcel import *

def create_parcel(id, leftcorner, rightcorner, color, value):
    '''
    Function that creates a parcel with the given attributes
    in: id - int > 0 , leftcorner, rightcorner is a point, color is a nonempty string, value is a string >0
    out: parcel - parcel
    raise ValueError if the area is smaller than 0.
    '''
    
    new_parcel = parcel(id, leftcorner, rightcorner, color, value)
    validate_parcel(new_parcel)
    return new_parcel

def search_parcel(lst,parcel):
    '''
    Function that searchs a parcel in the list
    out: r = position of parcel
            -1 if the elem doesn't exist
    '''
    
    for i in range(0,len(lst)):
        if get_id(lst[i]) == get_id(parcel):
            return i
    return -1
def remove_parcel(lst, parcel):
    '''
    Function that remove a parcel from the list
    out: lst' = lst without the parcel parcel
    '''
    position = search_parcel(lst, parcel)
    if position !=-1:
        lst.remove(lst, position)
    return lst    

def parcel_in_parcel( parcel1 , parcel2):
    '''
    function that returns True if the right corner of parcel 2 is in parcel 1 False if the left corner is in parce3l 1
    '''
    right = get_right_corner(parcel1)
    left = get_left_corner(parcel1)
    right_x = get_right_corner(parcel2)
    left_x = get_left_corner(parcel2)
    if (left_x[1] < left[1] and left_x[1]> right[1] and left_x[0] > left [0] and left_x[0]< right[0]):
         return False
    else:
        return True 

def big_value(parcel1, parcel2):
    value = get_value(parcel1)* get_area(parcel1)+get_value(parcel2)*get_area(parcel2)
    return value/(get_area(parcel1) + get_area(parcel2))

def add_parcel(lst, id, leftcorner, rightcorner, color, value):
    '''
    Function that adds a parcel to the list
    '''
    
    new_parcel = create_parcel(id, leftcorner, rightcorner, color, value)
    right = get_right_corner(new_parcel)
    left = get_left_corner(new_parcel)
    ok=0
    for x in lst :
        right_x = get_right_corner(x)
        left_x = get_left_corner(x)
        if (left_x[1] < left[1] and left_x[1]> right[1] and left_x[0] > left [0] and left_x[0]< right[0]) or (right_x[1] < left[1] and right_x[1]> right[1] and right_x[0] > left [0] and right_x[0]< right[0]) :
            ok=1
            lst = remove_parcel(lst, x)
            r = parcel_in_parcel(x, new_parcel)
            bigv = big_value(x, new_parcel)
            if r == True:
                big_parcel = create_parcel(get_id(new_parcel), get_left_corner(new_parcel), get_right_corner(x), "gray", bigv)
            else:
                big_parcel = create_parcel(get_id(new_parcel), get_left_corner(x), get_right_corner(new_parcel), "gray", bigv)    
            lst.append(big_parcel)
    if ok==0:      
        lst.append(new_parcel)    
    