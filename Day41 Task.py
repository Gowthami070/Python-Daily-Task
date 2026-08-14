#1.Write a Python program to expand a string where each character is followed by a number indicating how many times that character should be repeated.
'''
Input: a3b2a3
Output: aaabbbaaa
'''
#
'''
def expand_string(string):
    result = ""
    i = 0
    while i < len(string):
        char = string[i]
        count = int(string[i + 1])
        result += char * count
        i += 2
    return result
string = input("Enter string: ")
print(expand_string(string))
'''
#2.Write a Python program to remove consecutive duplicate characters from a string.
'''
Input:
aaabbccdaa
Output:
abcda
'''
#
'''
def remove_duplicates(string):
    result = ""
    for char in string:
        if result == "" or char != result[-1]:
            result += char
    return result
string = input("Enter string: ")
print(remove_duplicates(string))
'''
#3.Write a Python program to reverse each word in a sentence while maintaining the original word order.
'''
Input:
Python is easy
Output:
nohtyP si ysae
'''
#
'''
def reverse_str(string):
    result = ""
    words = string.split()
    for word in words:
        result += word[::-1] + " "
    return result.strip()
string = input("Enter string: ")
print(reverse_str(string))
'''
#4.Write a Python function to remove all special characters from a string.
'''
Input : a@1#b
Output : a1b
'''
#
'''
def splchar_remove(string):
    result = ""
    for char in string:
        if char.isalnum():
            result += char
    return result
string = input("Enter input: ")
print(splchar_remove(string))
'''
#5.Write a Python function to reverse every alternate word in a sentence.
'''
Input : one two three four
Output : one owt three ruof
'''
def reverse_alternate(string):
    words = string.split()
    result = []
    for i in range(len(words)):
        if i % 2 == 0:
            result.append(words[i])
        else:
            result.append(words[i][::-1])
    return " ".join(result)
string = input("Enter string: ")
print(reverse_alternate(string))
