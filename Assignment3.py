1. Rewritten python pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
Program:
def computepay(hours,rate):
 if hours>40.0:
  p = rate * 40.0
  p = p+(1.5*rate*(hours-40))
 else:
  p = rate*hours
 return p
hours = float(raw_input("Enter worked hours: "))
rate = float(raw_input("Enter pay rate per hour: "))
print (computepay(hours,rate))
Output:
Enter worked hours: 45
Enter pay rate per hour: 10
Pay: 475.0


2. Rewritten python pay program using try and except so that your program handles non-numeric input gracefully by printing a message and 
exiting the program. The following shows two executions of the program:
Program:
hours=input("Enter Hours:")
try:
  int(hours)
  rate=input("Enter Rate:")
  int(rate)
  pay = int(hours) * int(rate) 
  int(pay)
  print("Pay:")
  print(pay)
except: 
  print("Error, please enter a numeric input.")
Output:
Enter Hours: 20
Enter Rate: nine
Error, please enter a numeric input.
Enter Hours: forty
Error, please enter a numeric input.


3. Python program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
 Score   Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
 < 0.6     F
Program:
score = float(raw_input("Enter score: "))
if score>1.0 or score<0.0 :
	print "Error"
elif score>=0.9 :
  	print 'A'
elif score>=0.8 :
    print 'B'
elif score>=0.7 :
    print 'C'
elif score>=0.6 :
    print 'D'
else :
    print 'F' 
Output:
Enter score: 0.95
A
Enter score: perfect
Error

