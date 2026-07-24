#1.Given a list of integers, use a dictionary to count the frequency of each element and print the element that occurs the most.
'''
Input: Enter the number of elements: 8
       Enter the elements: 2 3 2 5 2 3 5 2
Output: Most Frequent Element: 2
        Frequency: 4
'''
#
'''
n=int(input("Enter the no.of elements:"))
nums=list(map(int,input("Enter the elements:").split()))
frequency={}
for i in nums:
    if i in frequency:
        frequency[i]=frequency[i]+1
    else:
        frequency[i]=1
print(frequency)
max_element=None
max_frequency=0
for key,value in frequency.items():
    if value > max_frequency:
        max_frequency=value
        max_element=key
print("Most frequennt element:",max_element)
print("Frequency:",max_frequency)
'''
#2.Given a list of words, use a dictionary to group the words based on their first letter.
'''
Input:
Enter the number of words: 6
Enter the words: apple ant ball bat cat carrot
Output:
{
'a': ['apple', 'ant'],
'b': ['ball', 'bat'],
'c': ['cat', 'carrot']
}
'''
#
'''
n=int(input("Enter the no.of words:"))
words=input("Enter:").split()
group={}
for word in words:
   first=word[0]
   if first not in group:
       group[first]=[]
   group[first].append(word)
print(group)
'''
#3.Given two dictionaries, check whether they contain the same key-value pairs.
'''
Input:
Dictionary 1:
{'a': 10, 'b': 20, 'c': 30}
Dictionary 2:
{'a': 10, 'b': 20, 'c': 30}
output: Equal
'''
#
'''
Dict1={'a': 10, 'b': 20, 'c': 30}
Dict2={'a': 10, 'b': 20, 'c': 30}
if Dict1==Dict2:
    print("Equal")
else:
    print("Not Equal")
    '''
#4.Given a list of tuples, where each tuple contains a key and a value, convert it into a dictionary.
'''
Input:
Enter the number of tuples: 4
('id',101)
('name','John')
('age',22)
('city','Hyderabad')
Output:
{
'id': 101,
'name': 'John',
'age': 22,
'city': 'Hyderabad'
}
'''
#
'''
n=int(input("Enter:"))
result={}
for i in range(n):
    key=input("Enter key:")
    value=input("Enter the value:")
    if value.isdigit():
        value=int(value)
    result[key]=value
print(result)
'''
#5.Given a number, use a dictionary to count the frequency of each digit.
'''
Input: 122334455561
Output:
{
'1': 2,
'2': 2,
'3': 2,
'4': 2,
'5': 3,
'6': 1
}
'''
#
'''
x=input("Enter:")
frequency={}
for i in x:
    if i in frequency:
        frequency[i]=frequency[i]+1
    else:
        frequency[i]=1
print(frequency)
'''
