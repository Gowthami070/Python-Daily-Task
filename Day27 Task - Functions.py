#1.Write a function reverse_string(text) that returns the reverse of the given string without using slicing ([::-1])?
'''
Sample Input:Python
Sample Output:nohtyP
'''
#
'''
def reverse_string(text):
    result=""
    for i in range(len(text)-1,-1,-1):
        result=result+text[i]
    return result
text="Python"
res=reverse_string(text)
print(res)
'''
#2.Write a function remove_duplicates(text) that removes duplicate characters while preserving the original order?
'''
Sample Input:programming
Sample Output:progamin
'''
#
'''
def remove_duplicates(text):
    duplicates=""
    for i in text:
        if i not in duplicates:
            duplicates+=i
    return duplicates
text="programming"
res=remove_duplicates(text)
print(res)
'''
#3.Write a function first_unique(text) that returns the first non-repeated character?
'''
Sample Input:swiss
Sample Output:w
'''
#
'''
def non_rep(st):
    for i in st:
        if st.count(i)==1:
            return i
st="swiss"
res=non_rep(st)
print(res)
'''
#4.Write a function replace_vowels(text) that replaces every vowel with *?
'''
Sample Input:Python Programming
Sample Output:Pyth*n Pr*gr*mm*ng
'''
#
'''
def replace_vowels(text):
    result=""
    for i in text:
        if i in "aeiouAEIOU":
            result+='*'
        else:
            result+=i
    return result
text="Python Programming"
res=replace_vowels(text)
print(res)
'''
#5.Write a function reverse_words(sentence) that reverses every word while keeping the word order unchanged?
'''
Sample Input:Hello Python
Sample Output:olleH nohtyP
'''
#

def reverse_string(text):
    result=""
    for i in text:
        result=result+i[::-1]+' '
    return result
text=input("enter:").split()
res=reverse_string(text)
print(res)

