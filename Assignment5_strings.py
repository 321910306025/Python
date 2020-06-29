1. Python program to count the number of characters (character frequency) in a string.
Program:
test_str = "Heena Kouser"
  all_freq = {} 
for i in test_str: 
    if i in all_freq: 
       all_freq[i] += 1
    else: 
       all_freq[i] = 1
print ("Count of all characters in Heena Kouser is :\n "
Output:
Count of all characters in Heena Kouser is: 
{'H': 1, 'e': 3, 'n': 1, 'a': 1, ' ': 1, 'K': 1, 'o': 1, 'u': 1, 's': 1, 'r': 1}


2. Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Program:
def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]
  return str1
print(change_char('Heena'))
Output:
He$na

3. Python function that takes a list of words and returns the length of the longest one.
Program:
a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=input("Enter element" + str(x+1) + ":")
    a.append(element)
max1=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>max1):
       max1=len(i)
       temp=i
print("The word with the longest length is:")
print(temp)
Output:
Enter the number of elements in list:3
Enter element1:"Bangalore"
Enter element2:"Mumbai"
Enter element3:"Delhi"
The word with the longest length is:
Bangalore


4. Python program to remove the nth index character from a nonempty string.
Program:
def remove(string, n):  
      first = string[:n]   
      last = string[n+1:]  
      return first + last
string=raw_input("Enter the sring:")
n=int(input("Enter the index of the character to remove:"))
print("Modified string:")
print(remove(string, n))
Output:
Enter the sring:Bilal
Enter the index of the character to remove:3
Modified string:
Bill


5. Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Program:
def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]
  return new_a + ' ' + new_b
print(chars_mix_up('Biena', 'Helal'))
Output:
Heena Bilal

                            
