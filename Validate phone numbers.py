"""

Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.

A valid mobile number is a ten digit number starting with a 7,8 or 9.

Concept

A valid mobile number is a ten digit number starting with a 7,8 or 9.

Regular expressions are a key concept in any programming language. A quick explanation with Python examples is available here. You could also go through the link below to read more about regular expressions in Python.

https://developers.google.com/edu/python/regular-expressions

Input Format

The first line contains an integer , the number of inputs.
 lines follow, each containing some string.

Constraints



Output Format

For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.

Sample Input

2
9587456281
1252478965
Sample Output

YES
NO
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
S = []
for _ in range(0,n):
    S.append((input()))

for i in S:
    if re.search(r'^[7-9]',str(i)) and str(i).isdigit() and len(i)==10:
        print('YES')
    else:
        print('NO')    
