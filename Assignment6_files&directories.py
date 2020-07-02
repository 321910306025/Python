1. Python program to open a file using try and except.
Program:
try:
    f = open("test.txt", "r")
except IOError:
    print "Oops, no file by that name"


2. Python program to split the data in a file. 
Program:
import logging.handlers
log = logging.getLogger()
fh = logging.handlers.RotatingFileHandler("D://Testfile.txt", 
 maxBytes=2**20*100, backupCount=100) 
# 100 MB each, up to a maximum of 100 files
log.addHandler(fh)
log.setLevel(logging.INFO)
f = open("D://biglog.txt")
while True:
     log.info(f.readline().strip())
Output:
Testfile.txt (end of file)
Testfile.txt.1
Testfile.txt.2
...
Testfile.txt.10 (start of file)


3. Python program to read the contents of a file using with statement.
Program:
L = ["Heena\n", "is\n", "a\n", "good\n", "girl.\n"] 
with open("myfile.txt", "w") as file1:
    file1.write("I am Heena.\n") 
    file1.writelines(L) 
    file1.close()
with open("myfile.txt", "r+") as file1: 
    print(file1.read())
Output:
I am Heena.
Heena 
is
a
good
girl.


4. Python program to remove file and directory.
Program:
#removing a file
import os 
print ("Enter 'quit' for exiting the program") 
filename = input('Enter the name of the file, that is to be deleted : ') 
if filename == 'quit': 
    exit() 
else: 
    print ('\nStarting the removal of the file !') 
    os.remove(filename) 
    print ('\nFile, ', filename, 'is successfully deleted.')
Output:
Enter 'quit' for exiting the program
Enter the name of the file, that is to be deleted : Testfile.txt
Starting the removal of the file !
File, Testfile.txt is successfully deleted.

#removing an empty directory
import os
os.rmdir("/github/python/assignments")
print('Directory successfully deleted.')
#removing a directory and contents
import shutil
shutil.rmtree("/home/heena/cache")
print('Directory successfully deleted.')
Output:
Directory successfully deleted.


5. Python program to create a list and access the elements in the list.
Program:


