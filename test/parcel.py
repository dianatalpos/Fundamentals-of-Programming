'''
Created on Nov 14, 2018

@author: Andrea
'''

def parcel(id, leftcorner, rightcorner, color, value):
    '''
    function that return a parcel with given attributes
    '''
    parcel = {"id" : id, "left corner": leftcorner, "right corner": rightcorner, "color" : color , "value": value }
    return parcel 


def get_id(parcel):
    return parcel["id"]

def get_left_corner(parcel):
    return parcel["left corner"]

def set_left_corner(parcel, point):
    parcel["left corner"] = point
    
def get_right_corner(parcel):
    return parcel["right corner"]

def set_right_corner(parcel, point):
    parcel["right corner"] = point

def get_color(parcel):
    return parcel["color"]

def set_color(parcel, color):
    parcel["color"] = color

def get_value(parcel):
    return parcel["value"]

def set_value(parcel, value):
    parcel["value"] = value
    
    
def get_area(parcel):
    right = get_right_corner(parcel)
    left = get_left_corner(parcel)
    return abs(right[0]-left[0])*abs(left[1]-right[1])