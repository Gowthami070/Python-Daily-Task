#1.Write a program to remove duplicates from a list using set?
'''
Input: [1, 2, 2, 3, 3, 3]
Output: [1, 2, 3]
'''
#
'''
x=[1, 2, 2, 3, 3, 3]
print(list(set(x)))
'''
#2.Return sorted elements of a set?
'''
Input: {3, 1, 2}
Output: [1, 2, 3]
'''
#
'''
x={3, 1, 2}
print(x)
'''
#3.Write a Python program to count how many elements are common among three sets?
'''
Sample Input:
A = {2, 4, 6, 8}
B = {4, 6, 8, 10}
C = {1, 4, 6, 12}
Sample Output:2
'''
#
'''
A = {2, 4, 6, 8}
B = {4, 6, 8, 10}
C = {1, 4, 6, 12}
x=A.intersection(B).intersection(C)
print(len(x))
'''
#4.Write a Python program to count how many perfect numbers are present in both the list and the tuple?
'''
Sample Input:
List  = [6, 12, 28, 20]
Tuple = (6, 28, 30, 496)
Sample Output:2
'''
#
'''
List  = [6, 12, 28, 20]
Tuple = (6, 28, 30, 496)
i=1
while i<=len(List):
    if List[i-1] in Tuple:
        print(List[i-1])
    i+=1
    '''
#5.Write a Python program to find the first element that is present in the list but missing in the tuple?
'''
Sample Input:
List  = [15, 20, 25, 30]
Tuple = (20, 30, 40)
Sample Output:15
'''
#
'''
List  = [15, 20, 25, 30]
Tuple = (20, 30, 40)

for element in List:
    if element not in Tuple:
        print(element)
        break
'''