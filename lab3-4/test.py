'''
Created on Oct 27, 2018

@author: Andrea
'''

from functions import *
from ui import *
 
def test_filter_type():
    lst=create_lst()
    lst=filter_type(lst, "gas")
    #assert len(lst[0]["Expenses"]) == 1
    print(len(lst[0]["Expenses"]))
def test_create_lst_type():
    lst=create_lst()
    list = create_lst_types(lst)
    
def test_sum_type():
    lst=create_lst()
    sum=sum_type(lst, "gas")
    assert sum == 667
    sum2=sum_type(lst,"water")
    assert sum2==250
    sum3= sum_type(lst, "electricity")
    assert sum3==0
def test_replace():
    lst = []
    lst = create_lst()
    lst = replace(lst, 15, "gas",1000)
    assert lst[0]["Expenses"][0]["amount"] == 1000
def test_remove_more():
    lst=[]
    lst = create_lst()
    lst = remove_more(lst, 10, 12)
    assert len(lst[5]["Expenses"])==0

def test_remove_ap():
    lst=[]
    lst=create_lst()
    lst= remove_ap(lst, 15)
    assert len(lst[0]["Expenses"]) ==0 


def test_remove_type():
    lst=[]
    lst=create_lst()
    lst=remove_type(lst, "gas")
    assert lst[0]["Expenses"][0]["type"] =="water"
    assert lst[0]["Expenses"][1]["type"] =="heating"
    #print(lst[0]["Expenses"][0]["type"])
def test_search_apartment_in_list():
    lst=[]
    flat = create_apartment(15)
    lst.append(flat)
    flat=create_apartment(12)
    lst.append(flat)
    position=search_apartment_in_list(lst, 15) 
    assert position == 0
    position2=search_apartment_in_list(lst, 2)
    assert position2 == -1 
    
    
def test_add_transaction():
    lst=[]
    lst.append(create_apartment(15))
    lst[0]=add_expense_to_apartment(lst[0], {"type":"gas", "amount": 125})
    lst=add_transaction(lst, 15, "water", 25)
    assert( lst[0]["Expenses"][1]["type"] )== "water"
    lst=add_transaction(lst, 15, "water", 25)
    assert (lst[0]["Expenses"][1]["amount"])==50
    lst=add_transaction(lst, 12, "gas", 30)
    assert lst[1]["Ap"] == 12
    '''
    lst = add_transaction(lst, 15, "gas", 23)
    lst = add_transaction(lst, 15, "water", 23)
    lst = add_transaction(lst, 15, "water", 27)
    assert lst[0]["Expenses"][1]["amount"] == 50
    assert lst[0]["Expenses"][0]["type"] == "gas"
    assert lst[0]["Expenses"][1]["type"] == "water"  
    '''
def test_validate_apartment():
    try:
        validate_transaction("sdf","gasdcdcd","12sds5")
    except ValueError as ve:
        assert ve != ""


def test_string_in_list():
    r = string_in_list("a", ["a","b","c"])
    assert r==True
    r2= string_in_list("0", ["a","b"])
    assert r2==False
                
def test_add_amount_in_expense():
    expense= create_expense("gas", 125)
    expense=add_amount_in_expense(expense, 25)
    assert expense["amount"]==150
    

def test_add_expense_to_apartment():
    flat = {"Ap": 15, "Expenses": []}
    expense = create_expense("gas", 125)
    flat = add_expense_to_apartment(flat, expense)
    expense=create_expense("water", 23)
    flat=add_expense_to_apartment(flat, expense)
    assert flat["Expenses"][0]["type"]=="gas"
    assert flat["Expenses"][0]["amount"]==125
    assert flat["Expenses"][1]["type"]=="water"
    
def test_search_type_in_apartment():
    flat = {"Ap": 15, "Expenses":[{"type": "gas", "amount": 125}]}
    p = search_type_in_apartment(flat, "gas")
    assert p == 0 
    flat2 = {"Ap": 15, "Expenses":[]}
    p2=search_type_in_apartment(flat2, "gas")
    assert p2 == -1
    
def test_get_type():
    expense = {"type":"gas", "amount": 125}
    assert get_type(expense) == "gas"
    
def test_get_amount():
    expense = {"type":"gas", "amount": 125}
    assert get_amount(expense)==125
    
def test_set_amount():
    expense = {"type": '', "amount": 0}
    expense = set_amount(expense, 15)
    assert get_amount(expense)==15

def test_set_type():
    expense = {"type": '', "amount": 0}
    expense = set_type(expense,"gas")
    assert get_type(expense) == "gas"

def test_create_expense():
    expense = create_expense("gas", 125)
    assert get_type(expense) == "gas"
    assert get_amount(expense) == 125
     
def test_get_apart():
    flat=create_apartment(10)
    assert get_apart(flat)==10
        
def test_set_apart():
    flat = {"Ap":0, "Expenses":[]}
    flat=set_apart(flat, 10)
    assert get_apart(flat)==10
    
def test_create_apartment():
    flat = create_apartment(5)
    assert get_apart(flat) == 5 

def tests():
    test_sum_type()
    test_remove_type()
    test_remove_ap()
    test_remove_more()
    test_create_apartment()
    test_set_apart()
    test_get_apart()
    test_get_amount()
    test_get_type()
    test_set_type()
    test_set_amount()
    test_create_expense()
    test_search_type_in_apartment()
    test_add_amount_in_expense()
    test_add_expense_to_apartment()
    test_string_in_list()
    test_add_transaction()
    test_search_apartment_in_list()
    test_replace()
    test_validate_apartment()
    test_create_lst_type()
    test_filter_type()