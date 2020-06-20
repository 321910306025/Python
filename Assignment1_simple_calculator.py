1. Program to design simple calculator for the operators
+  (Addition)
-  (subtraction)
*  (multiplication)
/  (division)
// (floor division)
** (exponent)
%  (modulus)

Program
num1 = int(input('Enter First number: '))
num2 = int(input('Enter Second number: '))
add = num1 + num2
dif = num1 - num2
mul = num1 * num2
div = num1 / num2
floor_div = num1 // num2
power = num1 ** num2
modulus = num1 % num2
print('Sum of ',num1 ,'and' ,num2 ,'is :',add)
print('Difference of ',num1 ,'and' ,num2 ,'is :',dif)
print('Product of' ,num1 ,'and' ,num2 ,'is :',mul)
print('Division of ',num1 ,'and' ,num2 ,'is :',div)
print('Floor Division of ',num1 ,'and' ,num2 ,'is :',floor_div)
print('Exponent of ',num1 ,'and' ,num2 ,'is :',power)
print('Modulus of ',num1 ,'and' ,num2 ,'is :',modulus)

Output
Enter First number: 9
Enter Second number: 5
Sum of 9 and 5 is: 14
Difference of 9 and 5 is: 4
Product of 9 and 5 is: 45
Division of 9 and 5 is: 1.8
Floor division of 9 and 5 is: 1
Exponent of 9 and 5 is: 59049
Modulus of 9 and 5 is: 4
