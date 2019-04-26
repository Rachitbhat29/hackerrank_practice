"""
Task 
You are given a string . It consists of alphanumeric characters, spaces and symbols(+,-). 
Your task is to find all the substrings of  that contains  or more vowels. 
Also, these substrings must lie in between  consonants and should contain vowels only.

Note : 
Vowels are defined as: AEIOU and aeiou. 
Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.

Input Format

A single line of input containing string .

Constraints


Output Format

Print the matched substrings in their order of occurrence on separate lines. 
If no match is found, print -1.

Sample Input

rabcdeefgyYhFjkIoomnpOeorteeeeet
Sample Output

ee
Ioo
Oeo
eeeee
Explanation

ee is located between consonant  and . 
Ioo is located between consonant  and . 
Oeo is located between consonant  and . 
eeeee is located between consonant  and .

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
x=0 
S = input()
found_pattern = re.finditer(r'w*([b-dB-Df-hF-Hj-nJ-Np-tP-Tv-zV-Z][aeiouAEIOU]{2,}[b-dB-Df-hF-Hj-nJ-Np-tP-Tv-zV-Z])',S)

for i in found_pattern:
    print(re.search(r'w*([aeiouAEIOU]{2,})',i.group(1)))
    x=1
    print(i)

if x==0:
    print(-1)    