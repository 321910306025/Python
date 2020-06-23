1. Python program to design simple calculator for the operators
+  (Addition)
-  (subtraction)
*  (multiplication)
/  (division)
// (floor division)
** (exponent)
%  (modulus).
Program:
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
Output:
Enter First number: 9
Enter Second number: 5
Sum of 9 and 5 is: 14
Difference of 9 and 5 is: 4
Product of 9 and 5 is: 45
Division of 9 and 5 is: 1.8
Floor division of 9 and 5 is: 1
Exponent of 9 and 5 is: 59049
Modulus of 9 and 5 is: 4


2. Python program to calculate simple interest.
Program:
P = float(input("Enter the principal amount : "))
N = float(input("Enter the number of years : "))
R = float(input("Enter the rate of interest : "))
SI = (P * N * R)/100
print("Simple interest : {}".format(SI))
Output:
Enter the principal amount: 100
Enter the number of years: 5
Enter the rate of interest : 5
Simple interest : 25.0

3. Python program to calculate area of a circle. 
Program:
PI = 3.14
r = float(input('Enter the radius of the circle :'))
area = PI * r * r
print("Area of the circle is : %.2f" %area)
#method 2
import math
r = float(input('Enter the radius of the circle :'))
area = math.pi * r * r
print("Area of the circle is : %.2f" %area)
Output:
Enter the radius of the circle: 3
Area of the circle is: 28.26

4. Python program to calculate area of a triangle.
Program:
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is: %0.2f' %area)
Output:
Enter first side: 5
Enter second side: 6
Enter third side: 7
The area of the triangle is: 14.70

5. Python program to temperature in Celsius to Fahrenheit.
Program:
celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f celsius is: %0.2f fahrenheit' %(celsius, fahrenheit))
Output:
Enter temperature in celcius: 37
37.00 celcius is: 98.60 fahrenheit'

6. Python program to calculate area of rectangle.
Program:
width = float(input('Enter the width of a rectangle: '))
height = float(input('Enter the height of a rectangle: '))
Area = width * height
print("\n Area of rectangle is: %.2f" %Area)
Output:
Enter the width of a rectangle: 6
Enter the height of a rectangle: 4
Area of rectangle is: 24.00

7. Python program to calculate perimeter of a square.
Program:
s=int(input("Enter Side : "))
perimeter=4*s
print("Perimeter of square: ",perimeter)
Output:
Enter side: 5
Perimeter of square is: 20

8. Python program to calculate circumference of a circle.
Program:
import math
radius = float(input("Enter the radius of the circle : "))
circumference = 2 * math.pi * radius
print("Circumference of the circle is : %.2f" % circumference)
Output:
Enter the radius of the circle: 10
Circumference of the circle is: 62.83

9. Python program to swap two numbers.
Program:
x = input('Enter value of x: ')
y = input('Enter value of y: ')
temp = x
x = y
y = temp
print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
Output:
Enter the value of X: 3
Enter the value of y: 2
The value of x after swapping is: 2
The value of y after swapping is: 3

10. Python program to take two inputs from user and check whether they are equal or not. 
Program:
a = input("Enter the first number: ")
b = input("Enter the second number: ")
if a == b:
  print "Both inputs are equal"
else:
  print "Your input is not equal."
Output:
Enter the first number: 5
Enter the second number: 8
Your input is not equal.

11. Python program to find square root.
Program:
import math
number = float(input("Enter any numeric Value : "))
squareRoot = math.sqrt(number)
print("The Square Root of a given number {0}  = {1}".format(number, squareRoot))
Output:
Enter any numeric value: 9
The Square Root of a given number 9.0 = 3.0

12. Python program to solve quadratic equation.
Program: 
import cmath  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
d = (b**2) - (4*a*c)  
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solutions are {0} and {1}'.format(sol1,sol2))
Output: 
Enter a: 8
Enter b: 16
Enter c: 8
The solutions are (-1+0j) and (-1+0j)



