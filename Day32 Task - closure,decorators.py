### 1. Write a Python program to create a basic decorator that prints a line of "=" * 20 before and after executing the function.
'''
Input:
Welcome to Python
Output:
====================
Welcome to Python
====================
Explanation:
The decorator should print a separator line before and after the original function.
'''
#
'''
def decfun(a):
    def innerfun():
        print('='*20)
        a()
        print('='*20)
    return innerfun
@decfun
def greet():
    print("Welcome to python")
greet()
'''
### 2. Write a Python program to create a basic decorator that converts the string returned by a function into uppercase.
'''
Input:
Hello Batch-85
Output:
HELLO BATCH-85
Explanation:
The decorator should execute the function, take the returned string, convert it to uppercase using upper(), and print the modified string.
'''
#
'''
def decfun(fun):
    def innerfun():
        y=fun()
        return y.upper()
    return innerfun
@decfun
def fun1():
    s="Hello Batch-86"
    return s
print(fun1())
'''
### 3. Write a Python program to create a basic decorator that prints the length of the string returned by the function.
'''
Input:
Programming
Output:
Programming
11
Explanation:
The decorator should execute the function, print its returned string, and then print its length.
'''
#
'''
def decfun(fun):
    def innerfun():
        y=fun()
        print(y)
        return len(y)
    return innerfun
@decfun
def fun1():
    s="Programming"
    return s
print(fun1())
'''
### 4. Write a Python program using Closure to create a function that checks whether a given string ends with a fixed suffix.
'''
Input:
Suffix = "ing"
String = "Programming"
Output:
True
Explanation:
Create an outer function that stores the suffix and returns an inner function to check whether any given string ends with that suffix.
'''
def suffix_check(suffix):
    def check(word):
        return word.endswith(suffix)
    return check
suffix=input("enter suffix:")
check=suffix_check(suffix)
text=input("Enter text:")
print(check(text))
### 5. Write a Python program to find the longest word whose characters are all unique in a given sentence.
'''
Input:
level world python amazing apple
Output:
python
Explanation:
A word is considered valid if no character repeats within the word. Among all valid words, print the longest one. If multiple valid words have the same maximum length, print the first one.
'''
#
'''
s="level world python amazing apple"
words=s.split()
longest=""
for i in words:
    if len(set(i))==len(i):
        if len(i)>len(longest):
            longest=i
print(longest)
'''









