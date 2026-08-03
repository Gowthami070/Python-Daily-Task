
#1)Given a string and a character, count how many times the character appears using recursion.
'''
Input: programming
       g
Output:2
'''
'''
def charappear(string, character):
    if string == "":
        return 0
    if string[0] == character:
        return 1 + charappear(string[1:], character)
    else:
        return charappear(string[1:], character)
string = "programming"
character = input("Enter the character: ")
result = charappear(string, character)
print(result)
'''
#2)Find the largest digit in a number using recursion.
'''
Input:527941
Output:9
'''
#
'''
def largest_digit(n):
    if n < 10:
        return n

    digit = n % 10
    largest = largest_digit(n // 10)

    if digit > largest:
        return digit
    else:
        return largest

num = int(input("Enter number: "))
print(largest_digit(num))
'''
#3)Given a string, print all possible subsequences using recursion.
'''
Input: abc
Output:
abc
ab
ac
a
bc
b
c
'''
#
'''
def subsequences(s, ans):
    if s == "":
        if ans != "":
            print(ans)
        return

    subsequences(s[1:], ans + s[0])
    subsequences(s[1:], ans)

string = input("Enter string: ")
subsequences(string, "")
'''
#4)Remove all spaces from a string using recursion.
'''
Input: hello world python
Output: helloworldpython
'''
#
'''
def remove_spaces(s):
    if s == "":
        return ""

    if s[0] == " ":
        return remove_spaces(s[1:])
    else:
        return s[0] + remove_spaces(s[1:])

string = input("Enter string: ")
print(remove_spaces(string))
'''
#5)Count the number of zeros in a given integer using recursion.
'''
Input:1002005
Output:4
'''
#
'''
def count_zeros(n):
    if n == 0:
        return 0
    if n % 10 == 0:
        return 1 + count_zeros(n // 10)
    else:
        return count_zeros(n // 10)
num = int(input("Enter number: "))
print(count_zeros(num))
'''
#6)Determine whether a number is prime using recursion.
'''
Input:29
Output: Prime
'''
#
'''
def is_prime(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)
num = int(input("Enter number: "))
if is_prime(num):
    print("Prime")
else:
    print("Not Prime")
    '''
#
'''
def decfun(fun):
    def innerfun():
        x=fun()
        return x.swapcase()
    return innerfun
@decfun
def fun1():
    name="HeLOl wOrLd"
    return name
res=fun1()
print(res)
'''
