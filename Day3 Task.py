#1. Write a program to print all numbers from 1 to n that leave a remainder of 1 when divided by 3.
'''
Input:
10

Output:
1 4 7 10

Explanation:
Print numbers whose remainder is 1 when divided by 3.
'''
#
'''
n=int(input("Enter:"))
i=1
while i<=n:
    if i%3==1:
        print(i)
    i+=1
'''
#2. Write a program to count how many numbers between 1 and n are greater than 20.
'''
Input:
25

Output:
5

Explanation:
The numbers are 21, 22, 23, 24, and 25
'''
#
'''
n=int(input("Enter:"))
cnt=0
i=1
while i<=n:
    if i>=20:
        cnt+=i
        print(i)
    i+=1
    '''
#3. Write a program to print all numbers between 1 and n except multiples of 5.
'''
Input:
15

Output:
1 2 3 4 6 7 8 9 11 12 13 14

Explanation:
Skip numbers 5, 10, and 15.
'''
#
'''
n=int(input("Enter:"))
i=1
while i<=n:
    if i%5!=0:
        print(i)
    i+=1
'''
#4. Write a program to find the sum of all numbers between m and n.
'''
Input:
3 7

Output:
25

Explanation:
3 + 4 + 5 + 6 + 7 = 25
'''
#
'''
n=int(input("enter:"))
i=int(input("enter:"))
sum=0
while i<=n:
    sum+=i
    i+=1
print(sum)
'''
#5.Write a program to count the number of odd numbers between m and n.
'''
Input:
5 15

Output:
6

Explanation:
The odd numbers are 5, 7, 9, 11, 13, and 15.
'''
#
'''
n=int(input("enter:"))#15
m=int(input("enter:"))#5
cnt=0
while m<=n:#5<=15--t
    if m%2!=0:#5%2!=0--t
        cnt+=1#0+5=5
    m+=1#5+1=6
print(cnt)#1
'''
#6.Write a program to print all multiples of a given number that are less than n.
'''
Input:
Number = 6
Limit = 40

Output:
6 12 18 24 30 36

Explanation:
Print multiples of 6 less than 40.
'''
#
'''
n=int(input("enter:"))
i=int(input("enetr:"))
while i<=40:
    if i%n==0:
        print(i)
    i+=1
'''
#7.Write a program to find the sum of numbers that are divisible by 4 between 1 and n.
'''
Input:
12

Output:
24

Explanation:
4 + 8 + 12 = 24
'''
#
'''
n=int(input("enter:"))
sum=0
i=1
while i<=n:
    if i%4==0:
        sum+=i
    i+=1
print(sum)
'''
#8.Write a program to print numbers from n to 1 by decreasing 2 each time.
'''
Input:
10

Output:
10 8 6 4 2

Explanation:
Reduce the value by 2 after every iteration.
'''
#
'''
n=int(input("enter:"))
while n>0:
    print(n)
    n-=2
'''
#9.Write a program to count how many numbers between 1 and n are not divisible by 3.
'''
Input:
10

Output:
7

Explanation:
The numbers are 1, 2, 4, 5, 7, 8, and 10.
'''
#
'''
n=int(input("Enter:"))
i=1
cnt=0
while i<=n:
    if i%3!=0:
        cnt+=1
    i+=1
print(cnt)
'''
