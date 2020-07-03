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
