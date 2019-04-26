"""
Sample Input

9 27
Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int,input().split(' '))

for i in range(1,n,2):
    str= '.|.'
    for j in range(1,i):
        str= str+'.|.'
    print(str.center((m),'-'), end="")    
    print("\r")
print('WELCOME'.center(m,'-'))    
for i in range(n-2,0,-2):
    str= '.|.'
    for j in range(i,1,-1):
        str= str+'.|.'
    print(str.center((m),'-'), end="")    
    print("\r")
