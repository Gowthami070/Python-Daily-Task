#1.Write a program to display the floor numbers in a building using a while loop?
'''
Output:
Floor 1
Floor 2
Floor 3
Floor 4
Floor 5
'''
#
'''
n=int(input("enter:"))
i=1
while i<=n:
    print("floor",i)
    i=i+1
    '''
#2.Write a program to display the days remaining for an event using a while loop?
'''
Input:
5

Output:
5 Days Left
4 Days Left
3 Days Left
2 Days Left
1 Day Left
'''
#
'''
n=int(input("enter:"))

while n>0:
    print(n,"Days Left")
    n=n-1
    '''
#3.Write a program to display the first 10 customer token numbers in a bank using a while loop?
'''
Output:
Token 1
Token 2
Token 3
...
Token 10
'''
#
'''
i=1
while i<=10:
    print("Token",i)
    i=i+1
    '''
#4.Write a program to display bus stop numbers from 1 to n using a while loop?
'''
Input:
6

Output:
Bus Stop 1
Bus Stop 2
Bus Stop 3
Bus Stop 4
Bus Stop 5
Bus Stop 6
'''
#
'''
n=int(input("enter:"))
i=1
while i<=n:
    print("Bus Stop",i)
    i=i+1
'''
#5.Write a program to display the first n levels of a game using a while loop?
'''
Input:
5

Output:
Level 1
Level 2
Level 3
Level 4
Level 5
'''
#
'''
n=int(input("Enter:"))
i=1
while i<=n:
    print("Level",i)
    i=i+1
'''
#6.Write a program to find the sum of all numbers from 1 to n that are divisible by 3 using a while loop?
'''
Input:
10

Output:
18
'''
#
'''
n=int(input("Enter:"))#10
sum=0
i=1
while i<=10:
    if i%3==0:
        sum=sum+i
    i=i+1
print(sum)
'''
#7.Write a program to count how many numbers between 1 and n are divisible by 5 using a while loop?
'''
Input:
25

Output:
5
'''
#
'''
n=int(input("Enetr:"))
i=1
cnt=0
while i<=n:
    if i%5==0:
        cnt=cnt+1
    i=i+1
print(cnt)
'''
#8.Write a program to print all numbers between 1 and n that are divisible by both 2 and 3 using a while loop?
'''
Input:
20

Output:
6 12 18
'''
#
'''
n=int(input("enter:"))
i=1
while i<=n:
    if i%2==0 and i%3==0:

        print(i)
    i=i+1
    '''
#9.Write a program to find the sum of squares of numbers from 1 to n using a while loop?
'''
Input:
4

Output:
30

Explanation:
1² + 2² + 3² + 4² = 30
'''
#
'''
n=int(input("Enter:"))
i=1
sum=0
while i<=n:
    sum=sum+(i*i)
    i=i+1
print(sum)
'''
#10.Write a program to find the sum of cubes of numbers from 1 to n using a while loop?
'''
Input:
3

Output:
36

Explanation:
1³ + 2³ + 3³ = 36
'''
#
'''
n=int(input("Enter:"))
i=1
sum=0
while i<=n:
    sum=sum+(i*i*i)
    i=i+1
print(sum)
'''














