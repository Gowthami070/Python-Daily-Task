#1.Write a Python program to replace all negative numbers in the list with 0?
'''
Sample Input:[10, -5, 20, -8, 15, -2]
Sample Output:[10, 0, 20, 0, 15, 0]
'''
'''
x=[10, -5, 20, -8, 15, -2]
for i in x:
    if i<0:
        i==0
    print(i)
'''
#2.Write a Python program to check whether a given list is a palindrome or not?
'''
Sample Input: [1, 2, 3, 2, 1]
Sample Output: Palindrome List
'''
#
'''
x=[1, 2, 3, 2, 1]
y=[]
for i in x:
    i=i%10
    y.append(i)
if x==y:
    print("Palindrome")
else:
    print("not a palidrome")
'''

#3.Write a Python program to find all even numbers in a list and check whether each even number is a Perfect Number or not?
'''
Sample Input:[6, 8, 15, 28, 12, 5]
Sample Output:
6 -> Perfect Number
8 -> Not a Perfect Number
28 -> Perfect Number
12 -> Not a Perfect Number
'''
#
'''
x=[6, 8, 15, 28, 12, 5]
y=[]
for i in x:
    sum=0
    for j in range(1,i//2+1):
        if i%j==0:
            sum=sum+j
    if sum==i:
       print("Pefect number")
    else:
        print("Not a perfect number")
'''

#4.Write a Python program to find all prime numbers in a list and calculate their sum?
'''
Sample Input:[2, 4, 5, 9, 11, 15, 17]
Sample Output:
Prime Numbers: 2 5 11 17
Sum = 35
'''
#
'''
x=[2, 4, 5, 9, 11, 15, 17]
y=[]
for i in x:
    sum=0
    cnt=0
    for j in range(2,i//2+1):
        if i%j==0:
            break
        else:
            cnt=cnt+i
            if cnt==2:
                y.append(i)
                sum=sum+j
    print(y)
print(sum)
            
'''
#5.Write a Python program to find all perfect numbers in a list and print the largest perfect number?
'''
Sample Input:[6, 28, 12, 496, 20]
Sample Output:Largest Perfect Number = 496
'''
#
x=[6, 28, 12, 496, 20]
for i in x:
    k=0
    for j in range(1,i//2+1):
        if i%j==0:
        
