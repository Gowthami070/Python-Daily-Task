#1. Write a function to_lowercase(text) that converts all uppercase English letters (A-Z) into lowercase .
'''
Example:
Input:  "PyThOn"
Output: "python"
'''
#
'''
def to_lowercase(text):
    result=""
    for ch in text:
        if 'A'<=ch<='Z':
            result+=chr(ord(ch)+32)
        else:
            result+=ch
    return result
            
print(to_lowercase("PyThOn"))
'''
#2. Write a function to_uppercase(text) that converts lowercase letters (a-z) into uppercase letters without using .upper().
    #Use ord() and chr().
'''
Example:
Input:  "hello World"
Output: "HELLO WORLD"
'''
#
'''
def to_uppercase(text):
    result=""
    for ch in text:
        if 'a'<=ch<='z':
            result+=chr(ord(ch)-32)
        else:
            result+=ch
    return result
            
print(to_uppercase("hello World"))
'''
#3. Write a function my_capitalize(text) that converts only the first character of a string to uppercase using ASCII values.
'''
Example:
Input:  "python programming"
Output: "Python programming"
'''
#
'''
def my_capitalize(text):
    if text=="":
        return text
    first=text[0]
    if 'a'<=first<='z':
        first=chr(ord(first)-32)
    return first+text[1:]
        
print(my_capitalize("python programming"))
''' 
#4. Write a function analyze_string(text) that counts and returns:
'''
Uppercase characters
Lowercase characters
Digits
Spaces
Special characters
Example:
Input: "PyThon 123!"
Expected result conceptually:
Uppercase: 2
Lowercase: 4
Digits: 3
Spaces: 1
Special: 1
'''
def analyze_string(text):
    uppercase = 0
    lowercase = 0
    digits = 0
    spaces = 0
    special = 0
    for ch in text:
        if 'A' <= ch <= 'Z':
            uppercase = uppercase + 1
        elif 'a' <= ch <= 'z':
            lowercase = lowercase + 1
        elif '0' <= ch <= '9':
            digits = digits + 1
        elif ch == ' ':
            spaces = spaces + 1
        else:
            special = special + 1
    return uppercase, lowercase, digits, spaces, special
Input = "PyThon 123!"
result = analyze_string(Input)
print("Uppercase:", result[0])
print("Lowercase:", result[1])
print("Digits:", result[2])
print("Spaces:", result[3])
print("Special:", result[4])
        
