#1.A movie theater has 20 seats. Seats with numbers divisible by 5 are reserved. Write a program to display only the available seat numbers?
'''
Input:20
Output:1 2 3 4 6 7 8 9 11 12 13 14 16 17 18 19

Explanation:
Skip seat numbers that are divisible by 5.
'''
#
'''
i=1
while i<=20:
    if i%5!=0:
        print(i,end=" ")
    i+=1
'''
#2.A company issues employee IDs from 1001 to 1020. Write a program to count how many employee IDs are even?
'''
Output:10

Explanation:
Count the IDs that are divisible by 2.

'''
#
'''
n1=1001
n2=1020
i=n1
cnt=0
while i<=n2:
    if i%2==0:
        cnt+=1
    i+=1
print(cnt)
'''
#3.A game contains 15 levels. Bonus rewards are given for levels divisible by 3. Write a program to display all bonus levels?
'''
Input:15
Output:3 6 9 12 15

Explanation:
Display levels that are divisible by 3.
'''
#
'''
i=1
while i<=15:
    if i%3==0:
        print(i,end=" ")
    i+=1
'''

#4.A library contains books numbered from 1 to 50. Write a program to count how many book numbers are multiples of 7?
'''
Input:50
Output:7

Explanation:
The book numbers are 7, 14, 21, 28, 35, 42 and 49.
'''
#
'''
i=1
cnt=0
while i<=50:
    if i%7==0:
        cnt+=1
    i+=1
print(cnt)
'''

#5.Write a program to find the first number greater than 100 that is divisible by both 7 and 9 using a while loop?
'''
Output:126

Explanation:
Continue checking numbers until a number divisible by both 7 and 9 is found.

'''
#
'''

i=100
while i>=100:
    if i%7==0 and i%9==0:
        print(i)
        break
    i+=1
    '''

#6.Write a program to print all numbers from 1 to n whose square is less than 50?
'''
Input:20
Output:1 2 3 4 5 6 7

Explanation:
The squares of these numbers are less than 50
'''
#
'''
n=int(input("enter:"))
i=1

while i<=n:
    if i**2<50:
        print(i)

    i+=1
 '''
#7.Write a program to count how many numbers between m and n are perfect squares.
'''
Input:1 20
Output:4

Explanation:1, 4, 9, and 16 are perfect squares.
'''
n1=int(input("enter:"))
n2=int(input("enter:"))
cnt=0
while n1<=n2:
    if n1**2<=n2:
        cnt=cnt+1
    print(cnt)






