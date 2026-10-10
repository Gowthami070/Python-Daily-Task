#1.Write a function second_character(text) that returns the second occurrence of a character that is different from the first character.
'''
Input: "aaabbc"
Output: "b"
'''
#
'''
def second_character(text):
    first = text[0]
    for i in text:
        if i != first:
            return i
text="aaabbc"
res=second_character(text)
print(res)
'''
#2.Write a function replace_vowels(text) that replaces every vowel with *.
'''
Input: "hello world"
Output: "h*ll* w*rld"
'''
#
'''
def replace_vowels(text):
    result = ""
    for i in text:
        if i in "aeiouAEIOU":
            result += "*"
        else:
            result += i
    return result           
text="hello world"
res=replace_vowels(text)
print(res)
'''
#3.Write a function count_words(text) that counts the words .
'''
Input: "Python is very easy"
Output: 4
'''
#
'''
def count_words(text):
    word=text.split()
    return len(word)
text="Python is very easy"
res=count_words(text)
print(res)
'''
#4.Write a function find_longest_word(text) that returns the longest word in a sentence.
'''
Input: "Python makes programming easy"
Output: "programming"
'''
#
'''
def find_longest_word(text):
    words = text.split()
    longest = ""
    for i in words:
        if len(i) > len(longest):
            longest = i
    return longest
text="Python makes programming easy"
res=find_longest_word(text)
print(res)
'''
#4.Write a function is_anagram(a, b) that checks whether two strings contain the same characters with the same frequencies.
'''
Input: "listen", "silen"
Output: True
'''
#
'''
def is_anagram(a, b):
    if sorted(a)==sorted(b):
        return True
    return False
a="listen"
b="silent"
res=is_anagram(a, b)
print(res)
'''
