'''
Created on Nov 14, 2018

@author: Andrea
'''
from functions import *


def test_create_parcel():
    id = 1
    leftcorner = [10,5]
    rightcorner = [1,0]
    color = "red"
    value = 15 
    try: 
        new_parcel = create_parcel(id, leftcorner, rightcorner, color, value)
        assert True
    except ValueError as ve:
        assert False
    bad_id=-1
    bad_leftcorner = [-5,-3]
    bad_rightcorner = [-3,-4]
    bad_color = ""
    bad_value = -15
    try:
        bad_parcel = create_parcel(bad_id, bad_leftcorner, bad_rightcorner,bad_color, bad_value)
        assert False
    except ValueError as ve:
        assert str(ve) =="The id must be a positive value!\nThe left corner must have positive values!\nThe right corner must have positive values!\nThe color must be nonempty!\nThe value must be a positive number!\nThe area of the parcel must be greater or equal than 25!\n"
        
def test_search_parcel(lst, parcel):       
    pass

def test_remove_parcel(lst, parcel):
    pass

def test_run():
    test_create_parcel()
    