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
L = ["Heena\n", "is\n", "a\n", "good\n", "girl\n"] 
with open("myfile.txt", "w") as file1:
    file1.write("Hello \n") 
    file1.writelines(L) 
    file1.close()
with open("myfile.txt", "r+") as file1: 
    print(file1.read())
Output:
Heena 
is
a
good
girl


4. Python program to remove file and directory.
Program:
