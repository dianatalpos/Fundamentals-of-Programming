'''
Created on Oct 31, 2018

@author: Andrea
'''
from functions import *

def ui_add(lst, param):
    try:
        validate_transaction(param[0],param[1], param[2])
        apart=int(param[0])
        type=param[1]
        amount=float(param[2])
        lst = add_transaction(lst,apart,type,amount)
    except ValueError as ve:
        print(ve)
            
    
def ui_remove(lst, param):
    types=["gas","water","heating","electricity","other"]
    if len(param) == 1:
        if string_in_list(param[0], types):
            lst = remove_type(lst, param[0])
        else:
            try:
                validate_ap(param[0])
                ap = int(param[0])
                try:
                    lst=remove_ap(lst,ap)
                except ValueError as pr:
                    print(pr)
            except ValueError as ve:
                print(ve)
    elif len(param)==3 :
        try:
            validate_remove_more_ap(param[0], param[1], param[2])
            apart1 = int(param[0])
            apart2 = int(param[2])
            lst = remove_more(lst,apart1,apart2)
            print_list(lst)
        except ValueError as br:
            print(br)
    else:
        print("Invalid command!The command must have at most 4 words!")

def ui_replace(lst, param):
    if len(param) == 4 and param[2]== "with":
        try:
            validate_transaction(param[0], param[1], param[3])
            apart = param[0]
            type = param[1]
            amount = param[3]
            try:
                lst = replace(lst,apart,type,amount)
            except ValueError as ve:
                print(ve)
        except ValueError as ve:
            print(ve)
    else:
        print("Invalid command!The command must have the next structure: replace apartment type with amount!")
def ui_list(lst, param):
    if len(param) == 0:
        print_list(lst)
    elif len(param)==1:
        try:
            validate_ap(param[0])
            ap = int(param[0])
            position = search_apartment_in_list(lst, ap)
            print_apart(lst[position])
        except ValueError as ve:
            print(ve)
    elif len(param)==2 and (param[0] == "<" or param[0]==">" or param[0] == "="):
        try:
            validate_amount(param[1])
            amount = float(param[1])
            list(lst,param[0],amount)
        except ValueError as ve:
            print(ve)
    else:
        print("Invalid command!")
        
def ui_sum(lst, param):
    types=["gas","water","heating","electricity","other"]
    if len(param)==1 and string_in_list(param[0], types):
        sum = sum_type(lst, param[0])
        print("The sum for all the " + param[0] + " expenses is: " + str(sum)) 
    else:
        print("Invalid command!")
        
def ui_sort(lst, param):
    if len(param)==1 and param[0] == "apartment" :
        new_lst = sorted(lst)
        print_list(new_lst)
    elif len(param)==1 and param[0] == "type":
        lst_types=create_lst_types(lst)
        list_sorted_type(lst_types)
    else:
        print:"Invalid command!"

def ui_filter(lst, param):
    if len(param) == 1 and param[0] == "gas":
        lst = filter_type(lst)  
        