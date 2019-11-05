'''
Created on Oct 31, 2018

@author: Andrea
'''

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


def set_apart(flat, ap):
    '''
       Function that sets the value of the apartement to the flat
       in: flat, ap
       pre: flat is an apartment with expenses, ap is an integer > 0
       out : flat' 
       post: flat' is the original flat with the value of apartment seted"
    '''
    flat["Ap"] = ap
    return flat

def get_apart (flat):
    '''
        Function that returns the number of the  apartment
        in: flat
        pre: flat is an apartment
        out: ap
        post ap- the number of the apartment
    '''
    return flat["Ap"]

def create_apartment (apartment):
    '''
        Function that creates an apartment
        in:  apartment
        pre: apartment - integer > 0
        out: flat
        post: flat is an apartment that contains the number of apartment and the expenses of that apartment
    '''
    flat = {"Ap": 0, "Expenses": [] }
    flat = set_apart(flat, apartment)
    return flat

def set_type(expense, type):
    '''
    Function that sets the value for the type of the expense
    in: expense, type
    pre: expense is an expense, type - string with value in { water, heating, electricity, gas, other}
    out: expense' 
    post: expense': is expense with the type set to type
    '''
    expense["type"] = type
    return expense

def get_type(expense):
    '''
    Function that return thetype of expense
    in: expense
    pre: expense is an expense
    out: type
    post: type string with value in { water, heating, electricity, gas, other}
    '''
    return expense["type"]

def set_amount(expense, amount):
    '''
    Function that sets the value for the amount of the expense
    in: expense, type
    pre: expense is an expense, amount is a float > 0
    out: expense'
    post: expense' is expense with the amount set to amount
    '''
    expense["amount"]=amount 
    return expense

def get_amount(expense):
    '''
     Function that return thetype of expense
     in: expense
     pre: expense is an expense
     out: amount
     post: amount float number > 0
    '''
    return expense["amount"]
    

def create_expense(type, amount):
    '''
        Function that creates an expense.
        in : type, amount
        pre: type - string with value in { water, heating, electricity, gas, other}
             amount - float > 0
        out: expense
        post expense is an expense that have a type and an amount 
    '''
    expense = {"type": '', "amount": 0 }
    expense = set_type(expense, type)
    expense = set_amount(expense, amount)
    return expense   

def search_type_in_apartment(flat, type):
    '''
        Function that finds if a type of expenses is in the apartment 
        in: flat, type
        pre:flat is an apartment, type is a type of expense
        out: p 
        post: p - the position of the type in Expenses from flat
              p == -1 when type is not in Expenses
              
    ''' 
    for i in range(0,len(flat["Expenses"])):
         if type == flat["Expenses"][i]["type"]:
             return i
    return -1

def add_amount_in_expense(expense, amount):
    '''
        Function that add an amount to an expense
        in:expense,amount
        pre: expense is an expense
             amount is a float > 0
        out: expense
    '''
    expense["amount"] += amount 
    return expense

def add_expense_to_apartment(flat, expense):
    '''
    Function that adds an expense to an apartment 
    in: flat, expense
    pre: flat is an apartment, expense is an expense
    out: flat' 
    post: flat' = flat U expense
    '''
    type = get_type(expense)
    position = search_type_in_apartment(flat, type) 
    if position == -1:
        flat["Expenses"].append(expense)
    else:
        flat["Expenses"][position] = add_amount_in_expense(flat["Expenses"][position], expense["amount"])
    return flat

def string_in_list(str,lst):
    '''
        Function that checks if a string is in the list
        in: str, lst 
        pre: str - string
             lst - a list with strings
        out: r
        post: r = True if str is in lst
                  False otherwise
    '''
    for i in range(0,len(lst)):
        if str==lst[i]:
            return True
    return False

def validate_ap(apartment):
    '''
    Function that validates if the value of apartment is a natural number
    in:apartment
    pre: apartment -integer > 0
    out:-
    post:-
    Raise ValueError if apartment is not an integer > 0
    '''
    error = ""
    try:
        x = int(apartment)
    except:
        error += "The apartment must be a natural number!\n"
    if len(error)> 0 :
        raise ValueError(error)
    

def validate_transaction(apartment,typee,amount):
    '''
    Function that validates the values of a new transaction.
    in:apartment,amount,type
    pre: apartment - integer > 0, 
         type - string with values in {gas, water, electricity, heating, other}
         amount - float > 0
    out: - 
    post: -
    Raise ValueError if apartment is not integer > 0, 
                        type is not string with values in {gas, water, electricity, heating, other}
                        amount is not float > 0
    '''
    error= ""
    try:
        x = int(apartment)
    except:
        error+="The number of apartment must be a natural number!\n"
    types=["gas","water","heating","electricity","other"]
    if string_in_list(typee,types) == False: 
        error+="The type must be gas,heating,water,electricity or other\n"
    try:
        x = int(amount)
    except:
        error+="The amount must be a number strictly greater then 0"
    if len(error)!= 0:
        error= "Invalid command!\n" + error
        raise ValueError(error)
def validate_amount(amount):
    '''
        Function that validates the value of amount
        in: amount
        pre: amount - float > 0
        out:-
        post:-
        Raise ValueError is amount is not float >0
    '''  
    try:
        x = float(amount)
        if x < 0 :
            raise ValueError("The number must be greater than 0!")
    except ValueError as ve:
        print("The number must be a real number!")
        
        
def search_apartment_in_list(lst,apartment):
    '''
    Function that checks if an apartment is in the list
    in: lst, apartment
    pre: lst a list with apartemnts
         apartment is the number of an apartment 
    out: p
    post: p = position of apartment in list if is in list
          p = -1 otherwise
    '''
    for i in range (0, len(lst)):
        if apartment == lst[i]["Ap"]:
            return i
    return -1

def add_transaction(lst,apartment,type,amount):
    '''
    Function that add a transaction to the list
    in: lst,apartment,type,amount
    pre: lst list with apartment and expenses 
        apartment - integer > 0
         type - string with values in {gas, water, electricity, heating, other}
         amount - float > 0
    out: lst'
    post: lst'=lst U transaction ( = apartment,type,amount)
    '''    
    position = search_apartment_in_list(lst, apartment)
    if position == -1:
        flat = create_apartment(apartment)
        lst.append(flat)
        position = len(lst)-1
    expense= create_expense(type, amount)
    lst[position]=add_expense_to_apartment(lst[position], expense)
    return lst

def remove_type(lst, type):
    '''
    Function that removes all the expenses with the type type
    in: lst, type
    pre: lst a list with transaction
         type is a string with values in "gas","water","heating","electricity","other"
    out:  lst'
    post: lst' = lst \ {"Ap": ,{"type": type,"amount": }
    '''
    for i in range(0,len(lst)):
        position = search_type_in_apartment(lst[i], type)
        if position != -1:
            for j in range(position, len(lst[i]["Expenses"])-1):
                lst[i]["Expenses"][j]=lst[i]["Expenses"][j+1]
    return lst            
                
def remove_ap(lst, apart):
    '''
    Function that removes all the expenses from apartment apart
    in:lst, apart
    pre: lst - a list with transaction
         apart- the number of an apartment
    out:lst'
    post:lst' = lst \ apart
    '''       
    position = search_apartment_in_list(lst, apart)
    if position != -1:
        lst[position]["Expenses"] = []
        return lst
    else:
        raise ValueError("This apartment doesn't exist!")


def remove_more(lst,ap1,ap2):
    '''
    Function that removes expenses from apartment ap1 to ap2
    in:ap1, ap2, lst
    pre: ap1 - the start of removing
         ap2 - the end of removing
         lst - the list of transactions
    out: lst'
    post: lst' = lst / all the expenses from ap1 to ap2
    '''
    for i in range (0,len(lst)):
        if get_apart(lst[i]) >= ap1 and get_apart(lst[i]) <= ap2:
            lst = remove_ap(lst, get_apart(lst[i]))
    return lst


def replace(lst,apart, type, amount):
    '''
    Function that replace the amount for the type type from apartment apart with amount
    in: apart, type, amount
    pre:lst - list with transactions  
        apartment - integer > 0
         type - string with values in {gas, water, electricity, heating, other}
         amount - float > 0
    out: lst' 
    post: lst' = the initial list with the amount changed for type from apartment 
    Raise ValueError if the expense for type doesn't exist
    '''
    position_apart = search_apartment_in_list(lst, apart)
    position = search_type_in_apartment(lst[position_apart], type)
    if position == -1:
        raise ValueError("The expense for "+ type +" doesn't exist! First you need to add the expense!")
    else:
        set_amount(lst[position_apart]["Expenses"][position], amount)
        return lst
         
def validate_remove_more_ap(ap1, str, ap2):
    '''
    Function that validates the input
    in: ap1,str,ap2
    pre:ap1 - integer > 0
        str = "to"
        ap2 - integer > a1
    '''
    error=""
    try:
        x = int(ap1)
    except:
        error+="The first value must be an integer!\n"
    if str !="to":
        error+="The third word must be 'to'!\n"
    try:
        x = int(ap2)
        if x < int(ap1):
            error+="The second value must be greater than the first one"
    except:
        error+="The second value must be an integer!\n"
    if len(error) !=0:
        raise ValueError(error)

def print_apart(flat):
    if len(flat["Expenses"])== 0 :
        print("Apartment "  + str(flat["Ap"]) + " has no expenses!")
    else:
        print("Apartment " + str(flat["Ap"]) + " has the next expenses :")
        for i in range(0, len(flat["Expenses"])):
            print("    ->" + flat["Expenses"][i]["type"] + " with the amount of " + str(flat["Expenses"][i]["amount"]))

def sum_apartment(lst):
    '''
    function that creates a new list with the total expenses for each apartment
    in: lst
     pre: lst - list with transaction
     out: lst'
     post: lst' - a new list with thesum of all the expenses for each apartment
    '''
    
    for i in range(0, len(lst)):
        sum=0
        for j in range(0, len(lst[i]["Expenses"])):
            sum=sum+ get_amount(lst[i]["Expenses"][j])
        lst[i]["Total"]=sum
    return lst
def change_position(lst, i,j):
    '''
    function that changes the elements from the positions i and j in new and lst
    in: lst , i, j
    pre: lst list with transactions
         i,j position in the list
    out:lst with the positions of i and j changed
    
    '''
    aux = lst[i]
    lst[i] = lst[j]
    lst[j] = aux 
    return lst
     
def sorted(lst):
    '''
     function that sorts the list by the total amount of expenses per apartment
     in: lst
     pre: lst - list with transaction
     out: lst'
     post: lst' - the initial list sorted
    '''
    chg= lst
    chg = sum_apartment(lst)
    for i in range(0,len(lst)-1):
        for j in range (i, len(lst)):
            if chg[i]["Total"]> chg[j]["Total"]:
                chg = change_position(lst,i,j)
    return chg
   
def sum_type(lst,type):
    '''
    Function that calculates the sum of the expenses with type type
        in:lst, type
        pre: lst list with transaction
             type  a string with value in:"gas","water","heating","electricity","other"
        out: sum
        post: sum is the sum of all the expenses with type type
    '''
    sum=0
    for i in range(0, len(lst)):
        position = search_type_in_apartment(lst[i], type)
        if position != -1:
            sum += get_amount(lst[i]["Expenses"][position])
    return sum

def create_lst_types(lst):
    '''
    Function that creates a new list with the types of expenses and the total amount of all the expenses from every apartments
    in: lst list with transaction
    out: lst_types - a list with the types and the expenses for every type
    '''
    apart=create_apartment(0)
    list = []
    exp = create_expense("gas", 0)
    apart=add_expense_to_apartment(apart, exp)
    exp = create_expense("heating", 0) 
    apart=add_expense_to_apartment(apart, exp)
    exp = create_expense("electricity", 0) 
    apart=add_expense_to_apartment(apart, exp)
    exp = create_expense("water", 0) 
    apart=add_expense_to_apartment(apart, exp)
    exp = create_expense("other", 0) 
    apart=add_expense_to_apartment(apart, exp)
    for i in range (0, len(lst)):
        for j in range(0,len(lst[i]["Expenses"])):
            ty = get_type(lst[i]["Expenses"][j])
            position=search_type_in_apartment(apart, ty)
            add_amount_in_expense(apart["Expenses"][position], get_amount(lst[i]["Expenses"][j]))
    for i in range (0, len(apart["Expenses"])-1):
        for j in range(i+1, len(apart["Expenses"])):
            if (get_amount(apart["Expenses"][i])> get_amount(apart["Expenses"][j])):
                change_position(apart["Expenses"], i, j)
            
    return apart["Expenses"]
    
    
def print_list(lst):
    for i in range(0,len(lst)):
        print_apart(lst[i])
        
def list(lst,relation, amount):
    '''
    Function that prints the transactions respecting a condition
    '''
    ok=0
    for i in range(0,len(lst)):  
        sum=0
        for j in range(0,len(lst[i]["Expenses"])):
            sum=sum+get_amount(lst[i]["Expenses"][j])
        if relation == "=" and sum == amount :
            print_apart(lst[i])
            ok=1
            print("    ->the total is " + str(sum))
        elif relation == ">" and sum > amount:
            print_apart(lst[i])
            print("    ->the total is " + str(sum))
            ok = 1
        elif relation == "<" and sum < amount:
            print_apart(lst[i])
            ok = 1  
            print("    ->the total is " + str(sum))
    if ok==0:
        print("There is no apartment that has the total expenses who respects the given condition.")        


def list_sorted_type(lst):
    for i in range(0,len(lst)):
        print("For " + get_type(lst[i]) +" expense, the total amount is: "+ str(get_amount(lst[i])))
        
def filter_type(lst, type):
    '''
    function that removes all the expenses without type
    in: lst, type
    pre: lst the list with preconditions
         type - a string with value in  { water, heating, electricity, gas, other}
    out: lst'
    post lst' - the initial list with all the expenses remove without the expenses with type type
    '''
    types = [ "water", "heating", "electricity", "gas", "other"]
    for i in range(0, len(types)):
        if type != types[i]:
            lst = remove_type(lst, types[i])
    return lst    
 
def filter_amount(lst, amount):
    lst = sum_apartment(lst)
     
        
        