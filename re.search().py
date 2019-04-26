"""
Task 
You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-). 
Your task is to find all the substrings of S that contains 2 or more vowels. 
Also, these substrings must lie in between 2 consonants and should contain vowels only.

Note : 
Vowels are defined as: AEIOU and aeiou. 
Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.

Input Format

A single line of input containing string S.

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

ee is located between consonant  d and f. 
Ioo is located between consonant k and m. 
Oeo is located between consonant p and r. 
eeeee is located between consonant t and t.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
x=0 
S = input()

while re.search(r'(=?(w*([b-dB-Df-hF-Hj-nJ-Np-tP-Tv-zV-Z][aeiouAEIOU]{2,}[b-dB-Df-hF-Hj-nJ-Np-tP-Tv-zV-Z])))',S):
    s = re.search(r'(=?(w*([b-dB-Df-hF-Hj-nJ-Np-tP-Tv-zV-Z][aeiouAEIOU]{2,}[b-dB-Df-hF-Hj-nJ-Np-tP-Tv-zV-Z])))',S).start()
    e = re.search(r'(=?(w*([b-dB-Df-hF-Hj-nJ-Np-tP-Tv-zV-Z][aeiouAEIOU]{2,}[b-dB-Df-hF-Hj-nJ-Np-tP-Tv-zV-Z])))',S).end()
    print(S[s+1:e-1])
    S =S[e-1:]
    x=1
    #print(i)

if x==0:
    print(-1)    
