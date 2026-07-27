#1. Write a Python function to return the *longest word* in a given sentence. If multiple words have the same maximum length, return the *first* one.
'''
Input:
Python is an amazing programming language
Output:
programming
Explanation:
Find the word with the maximum length. If there is a tie, return the word that appears first.
'''
#
'''
def largest_str(name):
    large_str=""
    for i in name:
        if len(i)>len(large_str):
            large_str=i
    return large_str
name="Python is an amazing programming language".split()
print(largest_str(name))
'''
### 2. Write a Python function to return a new string by moving all *uppercase letters* to the beginning, followed by all *lowercase letters*, while preserving their original order.
'''
Input:
PyThOnProGram
Output:
PTOPGramyhro
Explanation:
Collect all uppercase letters first, then append all lowercase letters without changing their relative order.
'''
#
'''
def moving_letter(name):
    upper=""
    lower=""
    for i in name:
        if i.isupper():
            upper+=i
        else:
            lower+=i
    return upper+lower
name="PyThOnProGram"
print(moving_letter(name))
'''
### 3. Write a Python function to return all characters that appear *exactly twice* in a string.
'''
Input:
programming
Output:
r g m
Explanation:
Return all characters whose frequency is exactly 2.
'''
#
'''
def char_twice(name):
    frequency=""
    for i in name:
        if name.count(i)==2 and i not in frequency:
                frequency+=i   
    return " ".join(frequency)
name="programming"
print(char_twice(name))
'''
### 4. Write a Python function to return the *first non-repeating character* in a string.
'''
Input:
aabbccddefg
Output:
e
Explanation:
Return the first character whose frequency is 1.
'''
#
'''
def non_repeating_char(name):
    for i in name:
        if name.count(i)==1:
            return i
name="aabbccddefg"
print(non_repeating_char(name))
'''
### 5. Write a Python function to check whether two strings are *rotations* of each other.
'''
Input:
s1 = "rotation"
s2 = "tionrota"
Output:
True
'''
#
'''
def isrotation(s1,s2):
    if len(s1)!=len(s2):
        return False
    return s2 in (s1+s2)
s1 = "rotation"
s2 = "tionrota"
print(isrotation(s1,s2))
'''
