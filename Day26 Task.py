#1. Write a Python program to count the number of uppercase letters, lowercase letters, digits, and special characters in a string?
'''
Sample Input:PyTh0n@123
Sample Output:
Uppercase = 2
Lowercase = 3
Digits = 4
Special Characters = 1
'''
#
'''
x="PyTh0n@123"
upper_cnt=0
lower_cnt=0
digit_cnt=0
spl_cnt=0
for i in x:
    if i.isupper():
        upper_cnt+=1
    elif i.islower():
        lower_cnt+=1
    elif i.isdigit():
        digit_cnt+=1
    else:
        spl_cnt+=1
print("Uppercase=",upper_cnt)
print("Lowercase=",lower_cnt)
print("Digits=",digit_cnt)
print("splecial characters=",spl_cnt)
'''
#2. Write a Python program to find the first non-repeated character in a string?
'''
Sample Input:programming
Sample Output:p
'''
#
'''
x="programming"
for i in x:
    if x.count(i)==1:
        print("First non repeating is:",i)
        break
    else:
        print("No reapeated characters")
        '''
#3.Write a Python program to remove duplicate characters from a string while preserving the original order?
'''
Sample Input:programming
Sample Output:progamin
'''
#
'''
x="programming"
duplicate=""
for i in x:
    if i not in duplicate:
        duplicate+=i
print(duplicate)
'''
#4.Write a Python program to find the longest word in a sentence?
'''
Sample Input:Python programming is very interesting
Sample Output:programming
'''
#
'''
x="Python programming is very interesting"
words=x.split()
large=words[0]
for i in words:
    if len(i)>len(large):
        large=i
print(large)
'''
#5.Write a Python program to reverse the order of words in a sentence?
'''
Sample Input:Python is easy to learn
Sample Output:learn to easy is Python
'''
#
'''
x="Python is easy to learn"
words=x.split()
reverse=words[::-1]
print(' '.join(reverse))
'''

