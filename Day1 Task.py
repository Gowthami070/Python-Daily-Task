#1. Write a program to print numbers from 1 to 10 using a while loop.
#Output:
#1 2 3 4 5 6 7 8 9 10
'''
i=1
while i<=10:
    print(i)
    i=i+1
    '''
#2. Write a program to print numbers from 10 to 1 using a while loop.
#Output:
#10 9 8 7 6 5 4 3 2 1
'''
i=10
while i>=1:
    print(i)
    i=i-1
    '''
#3. Write a program to print all even numbers from 1 to 20 using a while loop.
#Output:
#2 4 6 8 10 12 14 16 18 20
'''
i=1
while i<=20:
    if i%2==0:
        print(i)
    i=i+1
'''
#4. Write a program to print all odd numbers from 1 to 20 using a while loop.
#Output:
#1 3 5 7 9 11 13 15 17 19
'''
i=1
while i<=20:
    if i%2!=0:
        print(i)
    i=i+1
'''
#5. Write a program to find the sum of numbers from 1 to n using a while loop.
#Input:
#5

#Output:
#15
'''
n=int(input("enter:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print(sum)
'''
#6. Write a program to count the number of digits in a given number using a while loop.
#Input:
#45892
#Output:
#5
'''
n=int(input("Enter:"))
cnt=0
while n>0:
    n=n//10# we use this for we have to remove the last digit of the number and store it is in the cnt variable
    cnt=cnt+1
print(cnt)
'''
#7. Write a program to find the reverse of a number using a while loop.
#Input:
#12345
#Output:
#54321
'''
n=int(input("Enter:"))#123
rev=0
while n>0:#1>0--T
    dig=n%10#dig=1%10--1
    rev=rev*10+dig#0*10+1--1
    n//=10
print(rev)
'''
#8. Write a program to find the sum of digits of a number using a while loop.
#Input:
#456
#Output:
#15
'''
n=int(input("enter:"))
sum=0

while n>0:
    dig=n%10
    sum=sum+dig
    n=n//10
print(sum)
'''
#9. Write a program to print the multiplication table of a number using a while loop.
#Input:
#7
#Output:
#7 14 21 28 35 42 49 56 63 70
'''
n=int(input("Enter:"))
i=1
while i<=10:
    print(n,'*', i , '=' , n*i)
    i=i+1
'''
#10. Write a program to calculate the factorial of a number using a while loop.
#Input:
#5
#Output:
#120

n=int(input("enter:"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i=i+1
print(fact)

