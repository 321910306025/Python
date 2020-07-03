1. Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
Program:
import itertools      
d ={'1':['a','b'], '2':['c','d']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))
Output:
ac                                                                                                            
ad                                                                                                            
bc                                                                                                            
bd


2. Python program to create a dictionary from a string.
Program:
string = "{'A':13, 'B':14, 'C':15}"
Dict = eval(string) 
print(Dict) 
print(Dict['A']) 
print(Dict['C']) 
Output:
{'C': 15, 'B': 14, 'A': 13}
13
15


3. Python program to convert a tuple to a string.
Program:
def convertTuple(tup): 
    str =  ''.join(tup) 
    return str
tuple = ('H', 'e', 'e', 'n', 'a') 
str = convertTuple(tuple) 
print(str) 
Output:
Heena


4. Python program to slice a tuple.
Program:
tuplex = (3,2,1,9,1,0,3,0,6,0,2,5)
slice = tuplex[3:5]
print(_slice)
Output:
(9,1)


5. Python program to find the length of a tuple.
Program:
tuplex = tuple("Bilal")
print(tuplex)
print(len(tuplex))
Output:
('B', 'i', 'l', 'a', 'l')
5



