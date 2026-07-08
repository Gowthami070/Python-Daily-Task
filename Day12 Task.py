#1.Student Attendance
'''
Write a Python program using a for loop to read the attendance status (P for Present and A for Absent) of N students and count the total number of present and absent students?
Input:5
P
A
P
P
A
Output:
Present Students = 3
Absent Students = 2
'''
#
'''
n=int(input("Enter:"))
p=0
a=0
for i in range(1,n+1):
    i=input()
    if i=='p':
        p=p+1
    else:
        a=a+1
print("Present Students =",p)
print("Absent Students =",a)
'''
#2.Bus Ticket Collection
'''
Write a Python program using a for loop to read the ticket fare collected from N passengers and determine the passenger number who paid the highest fare.

Input:
5

30

50

45

80

60

Output:Passenger 4 Paid the Highest Fare
'''
#
'''
n=int(input("enter:"))
cnt=0
for i in range(1,n+1):
    i=int(input())
    if i>30:
       cnt=cnt+1 
print("Passanger",cnt,"Paid the Highest Fare")
'''    

#3.Write a Python program using a for loop to print all numbers between 1 and N whose product of digits is an even number?
'''
Input:15
Output:2 4 6 8 10 12 14
'''
#
'''
n=int(input("Enter:"))
for i in range(1,n):
    if i%2==0:
        print(i,end=' ')
        '''
#4.Write a Python program using a for loop to check whether a given number is an Armstrong Number or not?
'''
Input:153
Output: Armstrong Number

'''
#
'''
n=int(input("Enter:"))
s=str(n)
sum=0
m=len(s)
for i in s:
    i=int(i)%10
    arm=i**m
    sum=sum+arm
    i=i//10
if n==cnt:
    print("Armstrong Number")
else:
    print("Not a armstrong number")
'''

#5.Write a Python program to print the following pattern?
'''
Input:5
Output:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''
#

n=int(input("enter:"))
row_no=1
for i in range(1,n+1):
    for j in range(i):
        print(row_no,end=' ')
        row_no+=1
    print()

