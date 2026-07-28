#1.Write a Python program to create a function that returns the most frequently occurring character in a string?
'''
Input: mississippi
Output: i
'''
#
'''
def frequent_cnt(text):
    max_cnt=0
    result=""
    for i in text:
        count=text.count(i)
        if count>max_cnt:
            max_cnt=count
            result=i
    return result
text=input("Enter:")
res=frequent_cnt(text)
print(res)
'''
#2.Write a Python program to create a function that returns the common elements from three lists?
'''
Input:
[1,2,3,4]
[2,3,5]
[2,3,6]

Output:[2,3]
'''
#
'''
def common_element(list1,list2,list3):
    result=[]
    for i in list1:
        if i in list2 and i in list3:
            result.append(i)
    return result
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
list3=list(map(int,input().split()))
res=common_element(list1,list2,list3)
print(res)
'''
#3.Write a Python program to create a function that returns the longest word containing only unique characters?
'''
Input: cat apple world sky
Output: world
'''
#
'''
def unique_longest_word(text):
    longest=""
    words=text.split()
    for word in words:
        if len(word)==len(set(word)):
            if len(word)>len(longest):
                longest=word
    return longest
text=input("Enter:")
res=unique_longest_word(text)
print(res)
'''
#4.Consecutive Duplicate Removal
'''
Write a Python program to create a function that removes only consecutive duplicate characters.

Input:aaabbbbccdaa
Output:abcda
'''
#
'''
def consecutive_duplicate(text):
    word=text[0]
    for i in range(1,len(text)):
        if text[i]!=text[i-1]:
            word=word+text[i]
    return word
text=input("Enter:")
res=consecutive_duplicate(text)
print(res)
'''
#5.Username Generator

'''
Write a Python program to create a function that generates a username using:

First 3 characters of the first name
Last 3 characters of the last name
Birth year

Sample Input:
First Name : Rahul
Last Name : Sharma
Birth Year : 2002

Sample Output:rahrma2002
'''
#
'''
def generates_username(first,last,dob):
    username=first[:3]+last[-3:]+str(dob)
    return username
first=input("ENter:")
last=input("ENter:")
dob=int(input("Enter"))
res=generates_username(first,last,dob)
print(res)
'''
