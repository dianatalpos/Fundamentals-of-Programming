''''a = 1
b = [str(a), 1]
c = {a : a, str(b[1]) : b}

print(c)
print(type(a) == type(c[1]))

a = ['1']
print(type(a) == type(c[1]))
print(type(b[0]) == type(a))
print(str(a) in c)
print(str(a))
print('\n')
print(str(a)
'''

a = {}

a[rows] = [1]
a[columns] = [2]
a[values] = [5]

for i in range(0,3):
    ok = 1
    for j in range(0,3):
        if i in a[rows]:
            for k in range(len(a[rows])):
                if  i == a[rows][k] and j == a[columns][k]:
                    print (str(a[values[k]])+ " ")
                    ok =0
                    
        if ok==1:
            print("0 ")
    
    print('\n')
    
        
                     