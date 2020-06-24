1. Python program to take two numbers and add two numbers.
Program:
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
sum = float(num1) + float(num2)
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
Output:
Enter first number: 2
Enter second number: 3
The sum of 2.0 and 3.0 is 5.0


2. Python program that uses input to prompt a user for their name and then welcomes them.
Program:
name = input('Enter your name: ')
print("Welcome", name)
Output:
Enter your name: Heena
Welcome Heena


3. Python program to prompt the user for hours and rate per hour to compute gross pay.
Program:
hrs=input("Enter hour:")
rate=input("Eenter rate per hour:")
pay=float(hrs)*float(rate)
print("Pay:", pay)
Output:
Enter hour: 35
Enter rate per hour:2.75
Pay: 96.25


4.Assume that we execute the following assignment statements:
width = 1
height = 12.0
For each of the following expressions, write the value of the expression and the type (of the value of the expression).
    1. width / 2
    2. width / 2.0
    3. height / 3
    4. 1 + 2 * 5
 Use Python interpreter to check your answers.
Answer:
width = 17
height = 12.0
print type(width / 2)    # <type 'int'>
print type(width / 2.0)  # <type 'float'>
print type(height / 3)   # <type 'float'>
print type(1 + 2 * 5)    # <type 'int'>


5. Python program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.
Program:
celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f celsius is: %0.2f fahrenheit' %(celsius, fahrenheit))
Output:
Enter temperature in celcius: 37
37.00 celcius is: 98.60 fahrenheit

