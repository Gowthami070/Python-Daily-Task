#1.Write a Python program using a for loop to print the following alphabet pattern?
'''
Input:5
Output:
A
BB
CCC
DDDD
EEEEE
'''
#
'''
n=int(input("Enter:"))
for i in range(1,n+1):
    for j in range(i):
        print(chr(64+i),end='')
    print()
'''
#2.Write a Python program using a for loop to print the following alphabet pattern?
'''
Input:5
Output:
ABCDE
ABCD
ABC
AB
A
'''
#
'''
n=int(input("Enter:"))
for i in range(n,-1,-1):
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print()
'''

#3.Write a Python program using a for loop to calculate the total deposits and the average daily deposit for a bank over N days?
'''
Input:5
1000
1500
2000
1200
1800

Output:
Total Deposits = 7500
Average Daily Deposit = 1500.0

Explanation:
The first input represents the number of days (N).
The next N inputs represent the deposit amount for each day.
Calculate the total amount deposited over all N days.
Calculate the average daily deposit by dividing the total deposits by the number of days.
'''
#
'''
n=int(input("Enter:"))
sum=0
cnt=0
for i in range(1,n+1):
    days=int(input())
    if days>0:
        sum=sum+days
        cnt=cnt+1
print("Total Deposits =",sum)
avg=sum/cnt
print("Average Daily Deposit = ",avg)
'''
#4.Write a Python program using a for loop to find the second smallest number among N input numbers?
'''
Input:5
12
5
18
3
10

Output:
Second Smallest Number = 5

Explanation:
The first input represents the number of elements (N).
The next N inputs are the numbers.
Arrange the numbers in ascending order:
3 5 10 12 18
The smallest number is 3.
The second smallest number is 5.
Therefore, the output is:
Second Smallest Number = 5
'''
#
'''
n=int(input("Enter:"))
large=small=float('inf')
for i in str(n):
    for j in i:
        i=int(input())
        if i>large:
            small=large
            large=i
        if i>small and i<large:
            small=i
print("Small num is:",small)
   '''     

#5.Write a Python program using a for loop to check whether a given number is a Strong Number or not?
'''
Input:145
Output:Strong Number
'''
#

n=int(input("Enter:"))
sum=0
bkp=n
s=str(n)
for i in s:
    fact=1
    i=int(i)%10
    for i in range(1,i+1):
        fact=fact*i
    i=i//10
    sum=sum+fact
    print("sum:",sum)
if sum==bkp:
    print("Strong Number")
else:
    print("not a strong number")





