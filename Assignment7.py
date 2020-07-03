1. Python program to sum all the items in a dictionary.
Program:
def returnSum(myDict): 
       sum = 0
    for i in myDict: 
        sum = sum + myDict[i] 
        return sum
dict = {'a': 100, 'b':200, 'c':300} 
print("Sum :", returnSum(dict)) 
Output:
Sum : 600


2. Python program to demonstrate accessing an element from a dictionary.
Program:
Dict = {1: 'Hello', 'name': 'Bilal', 3: 'Heena'} 
print("Accessing a element using key:") 
print(Dict['name']) 
print("Accessing a element using key:") 
print(Dict[3])
Output:
Accessing a element using key:
Bilal
Accessing a element using key:
Heena


3. Python program to concate two dictionaries.
Program:
def Merge(dict1, dict2): 
    res = {**dict1, **dict2} 
    return res 
dict1 = {'a': 10, 'b': 8} 
dict2 = {'d': 6, 'c': 4} 
dict3 = Merge(dict1, dict2) 
print(dict3)
Output:
{'b': 8, 'a': 10, 'c': 4, 'd': 6}


4. Python program to add keys/values in a dictionary.
Program:
dict = {'key1':'Hk', 'key2':'and'}  
print("Current Dict is: ", dict)  
dict1 = {'key3':'Bilal', 'key4':'are', 'key5':'fabulous'}  
dict.update(dict1)  
dict.update(newkey1 ='Heena')  
print(dict)  
Output:
Current Dict is: {‘key2’: ‘and’, ‘key1’: ‘Hk’}
{‘newkey1’: ‘Heena’, ‘key4’: ‘are’, ‘key2’: ‘and’, ‘key1’: ‘Hk’, ‘key5’: ‘fabulous’, ‘key3’: ‘Bilal’}


5. Python program to find length of a dictionary.
Program:
dict = {'Name': 'Heena', 'Age': 18};
print "Length : %d" % len (dict)
Output:
Length : 2


6. Python program to remove items from a dictionary.
Program:
test_dict = {"Heena" : 18, "Bilal" : 21, "Ameena" : 18} 
print ("The dictionary before performing remove is : " + str(test_dict)) 
del test_dict['Ameena'] 
print ("The dictionary after remove is : " + str(test_dict)) 
Output:
The dictionary before performing remove is : {'Heena' : 18, 'Bilal' : 21, 'Ameena' : 18}
The dictionary after remove is : {'Heena' : 18, 'Bilal' : 21}

