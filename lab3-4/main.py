'''
Created on Oct 27, 2018

@author: Andrea
'''

from test import *


def menu():
    print("Menu:")
    print("     Add a new transaction to the list.('add apartment type amount')")
    print("     Print the expenses having a property ('list'/'list apartment'/'list {>,<,=} amount)")
    print("     Remove expenses from an apartment or more, for a specific type('remove apartment/apartment1 to apartment2/type'")
    print("     Replace an amount for a type from an apartment('replace apartment type with amount')")
    print("     The total amount for a given type('sum type')")
    print("     Print the list of apartments sorted by the total amount of expenses('sort apartment')")
    print("     Print the list of the types of expenses sorted ascending by amount of money('sort type')")
    print("     Filter the list of transactions by type or amount('filter type/ amount')")
    print("     Exit")

def create_lst():
    lst=[]
    lst=add_transaction(lst, 15, "gas", 125)
    lst=add_transaction(lst, 15, "water", 125)
    lst=add_transaction(lst, 15, "heating", 125)
    lst=add_transaction(lst, 12, "gas", 12)
    lst=add_transaction(lst, 12, "other", 25)
    lst=add_transaction(lst, 13, "gas", 15)
    lst=add_transaction(lst, 14, "water", 125)
    lst=add_transaction(lst, 14, "gas", 125)
    lst=add_transaction(lst, 15, "gas", 125)
    lst=add_transaction(lst, 13, "gas", 125)
    lst=add_transaction(lst, 11, "gas", 125)
    lst=add_transaction(lst, 10, "gas", 15)
    return lst
    

def run():
    lst = []
    lst=create_lst()
    while True:
        menu()
        x = input("Give a command:")
        new = x.split(" ")
        if new[0] == "add":
            ui_add(lst, new[1:])
        elif new[0] == "list":
            ui_list(lst, new[1:])
        elif new[0] == "sum":
            ui_sum(lst, new[1:])
        elif new[0] == "remove":
            ui_remove(lst, new[1:])
        elif  new[0] == "sort":
            ui_sort(lst, new[1:])
        elif new[0] == "replace":
            ui_replace(lst,new[1:])
        elif new[0] == "filter" :
            ui_filter(lst, new[1:])
        elif new[0] == "exit":
            return
        else:
            print("Invalid command!")


tests()
run()