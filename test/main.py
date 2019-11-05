'''
Created on Nov 14, 2018

@author: Andrea
'''

from tests import *
from functions import *

def ui_add_parcel(lst, param):
    if len(param)!=7:
        print("Invalid number of params!")
        return
    try:
        id = int(param[0])
    except ValueError as ve:
        print("The id must be an integer")
    try:
        left_x = int(param[1])
        left_y = int(param[2])
        left = [left_x, left_y]
    except ValueError as ve:
        print("The values of left corner must be integers")    
    try:
        right_x = int(param[3])
        right_y = int(param[4])
        right = [right_x, right_y]
    except ValueError as ve:
        print("The values of left corner must be integers")    
    try:  
        value = int(param[6])
    except ValueError as ve:
        print("The value of parcel must be an integer!")
    color = param[5]
    try:
        lst = add_parcel(lst,id, left, right, color, value)
    except ValueError as ve:
        print(ve)
        
        
def menu():
    print("1. Add a parcel to the list: add id left_corner.x lef_corner.y right_corner.x right_corner.y color value")
    print("0. Exit:'exit'")

def run():
    lst = []
    while True:
        menu()
        x = input("Give a command: ")
        new = x.split(" ")
        if x == "exit" :
            return
        elif new[0] == "add" :
            ui_add_parcel(lst, new[1:])
        else:
            print("Invalid command!")
test_run()
run()
