"""
You are given a string N. 
Your task is to verify that N is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

 Number can start with +, - or . symbol. 
For example: 
✔
+4.50 
✔
-1.0 
✔
.5 
✔
-.7 
✔
+.4 
✖
 -+4.5

 Number must contain at least  decimal value. 
For example: 
✖
 12. 
✔
12.0  

 Number must have exactly one . symbol. 
 Number must not give any exceptions when converted using float(N).

Input Format

The first line contains an integer T, the number of test cases. 
The next T line(s) contains a string N.

Constraints

Output Format

Output True or False for each test case.

Sample Input 0

4
4.0O0
-1.00
+4.54
SomeRandomStuff
Sample Output 0

False
True
True
False
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
S = []
x=0
for _ in range(0,n):
    S.append(input())   

for i in S:
    #print(i)
    if re.search(r'[+-]?\.{1}',(i)):
        try:
            float(i)
            if re.search(r'[+-]?\.{1}',(i)):
                #print(f, str(f))
                x =1
        except ValueError:
            x=0    
    else:
        x=0
        
    if x==1:
        print('True')
    else:
        print('False')  