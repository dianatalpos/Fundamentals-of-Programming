'''
Created on Nov 14, 2018

@author: Andrea
'''

from parcel import *

def validate_parcel(parcel):
    '''
    Function that validates the input for a parcel
    raise ValueError if the attributes of a parcel are not ok.
    '''
    errors = ""
    if get_id(parcel) <= 0:
        errors += "The id must be a positive value!\n"
    left = get_left_corner(parcel)  
    if left[0] < 0 or left[1] < 0 :
        errors += "The left corner must have positive values!\n"
    right = get_right_corner(parcel)
    if right[0] < 0 or right[1] < 0 :
        errors +=  "The right corner must have positive values!\n"
    if get_color(parcel) == "" :
        errors += "The color must be nonempty!\n"
    if get_value(parcel) < 0:
        errors += "The value must be a positive number!\n" 
    if get_area(parcel) < 25:
        errors += "The area of the parcel must be greater or equal than 25!\n" 
          
    if len(errors) > 0:
        raise ValueError(errors)