#1. Write a Python program to print the following pattern?
'''
Input:5
Output:

A
AB
ABC
ABCD
ABCDE
'''
#
'''
rows=int(input("enter:"))
for row_no in range(1,rows+1):
    for i in range(1,row_no+1):
        print(chr(64+i),end="")
    print()
    '''
#2. Write a Python program to print the following pattern?
'''
Input:5

Output:

*****
****
***
**
*
'''
#
'''
i=5
for i in range(i,0,-1):
    print('*'*i)
 
'''
#3. Write a Python program to print the following pattern.
'''
Input:
5

Output:

1
22
333
4444
55555
'''
#
'''
row=int(input("enter:"))
for i in range(1,row+1):
    for j in range(i):
        print(i,end='')
    print()
'''
#4. Write a Python program to print the following pattern?
'''
Input:5
Output:

12345
1234
123
12
1
'''
#
'''
row=int(input("enter:"))
n=row
while n>=1:
    i=1
    while i<=n:
        print(i,end='')
        i=i+1
    print()
    n=n-1
 '''

#5.Write a Python program using a for loop to read the runs scored in N matches and calculate the total runs?
'''
Input:5
45
62
78
30
55

Output:Total Runs = 270
'''
#

n=int(input("Enter:"))
sum=0
for i in range(1,n+1):
        i=int(input())
        sum=sum+i
print("Total Runs =",sum)




    

