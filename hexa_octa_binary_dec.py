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
from decimal import * 

def print_formatted(number):
    for i in range(1,number+1):
        numbers = numbers.append(Decimal(i))
        numbers = numbers.append(oct(i).replace("0o",""),'',hex(i).replace("0x",""),'',bin(i).replace("0b",""))

    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)