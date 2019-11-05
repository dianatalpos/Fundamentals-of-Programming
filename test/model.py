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
    
    
    
    