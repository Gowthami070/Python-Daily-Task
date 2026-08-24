#1. Write a Python function to count the frequency of each character in a string and represent the result as character followed by its frequency.
'''
Input: aaabcc
Output: a3b1c2
'''
#
'''
text="aaabcc"
frequency={}
for i in text:
    if i in frequency:
        frequency[i]=frequency[i]+1
    else:
        frequency[i]=1
result=""
for key,value in frequency.items():
    result=result+key+str(value)
print(result)
'''
#2. Write a Python function to check whether two lists are rotations of each other.
'''
Input:
[1, 2, 3, 4, 5]
[3, 4, 5, 1, 2]
Output: True
'''
list1=[1, 2, 3, 4, 5]
list2=[3, 4, 5, 1, 2]
if len(list1)!=len(list2):
    return False

#3. Write a Python program to create a new dictionary containing two keys, "Even" and "Odd", and store the original dictionary keys based on whether their values are even or odd.
'''
Input:
d = {"a": 12, "b": 25, "c": 18, "d": 31, "e": 40}
Output:
{"Even": ['a', 'c', 'e'],"Odd": ['b', 'd']}
'''
#4. Write a Python program to create a new nested tuple by removing duplicate elements from each inner tuple, while maintaining the original order.
'''
Input:
x = ((10, 20, 10, 30),(5, 5, 8, 10),(15, 20, 15, 25))
Output:
((10, 20, 30), (5, 8, 10), (15, 20, 25))
'''
