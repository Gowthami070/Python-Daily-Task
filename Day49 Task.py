#1.Find the length of the longest substring that contains no repeated characters.
'''
Input: "abcabcbb"
Output: 3
Because the longest substring without repeating characters is: "abc"
'''
#2.Write a function is_anagram(str1, str2) that checks whether two strings contain the same characters with the same frequency.
'''
Input: "listen", "silent"
Output: True
'''
#
'''
def is_anagram(str1, str2):
    if sorted(str1)==sorted(str2):
        return True
    else:
        return False
str1="listen"
str2="silent"
res=is_anagram(str1, str2)
print(res)
'''
#3.Write a function compress(text) that converts consecutive repeated characters into the character followed by its count.
'''
Input: "aaabbcccc"
Output: "a3b2c4"
'''
#
'''
def compress(text):
    result = ""
    count = 1
    for i in range(len(text)):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
        else:
            result += text[i] + str(count)
            count = 1
    return result
text="aaabbcccc"
res=compress(text)
print(res)
'''
#4.Write a function replace_vowels(text) that replaces each vowel with the next vowel: a → e e → i i → o o → u u → a Example:
'''
Input: "education"
Output: "idacetoun"
'''
#
'''
def replace_vowels(text):
    for i in text:
        vowels = {
        'a': 'e',
        'e': 'i',
        'i': 'o',
        'o': 'u',
        'u': 'a'
    }
    result = ""
    for ch in text:
        if ch in vowels:
            result += vowels[ch]
        else:
            result += ch
    return result
text="education"
res=replace_vowels(text)
print(res)
'''
#5.Write a function is_rotation(str1, str2) that checks whether str2 is a rotated version of str1.
'''
Input: "abcd", "cdab"
Output: True
'''
#
'''
def is_rotation(str1, str2):

str1="abcd"
str2="cdab"
res=is_rotation(str1, str2)
print(res)
'''
