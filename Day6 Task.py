#1. Write a Python program using a while loop to calculate the sum of the first N natural numbers and determine whether the sum is even or not.
'''
Input:10
Output:
Sum = 55
Not Even

Explanation:
The sum of the first 10 natural numbers is 55. Since 55 is not divisible by 2, the sum is not even.
'''
#
'''
n=int(input("enter:"))
i=1
sum=0
while i<=n:
        sum=sum+i
        i+=1
print("sum=",sum)
if sum%2==0:
    print("even")
else:
    print("not even")
    '''
#2. Write a Python program using a while loop to find the Greatest Common Divisor of two numbers.
'''
Input:24 36
Output:GCD = 12

Explanation:
12 is the largest number that divides both 24 and 36 exactly.

 '''
#
'''
n1=int(input("enter:"))
n2=int(input("enter:"))
if n1>n2:
        small=n1
else:
        small=n2
d=1
gcd=1
while d<=small:
        if n1%d==0 and n2%d==0:
                gcd=d
        d+=1
print("GCD is:",gcd)
'''
#3. Write a Python program using a while loop to check whether a given number is a prime number or not.
'''
Input:7
Output:Prime Number
Input:8
Output:Not Prime Number

Explanation:
A prime number is divisible only by 1 and itself.
'''
#
'''
n=int(input("enter:"))
if n<=1:
        print("not prime")
else:
        i=2
        while i<=n//2:
                if n%i==0:
                        print("Not prime")
                        break
                i+=1
        else:
                print("Prime number")

'''
#4. Write a Python program using a while loop to print all prime numbers from 1 to 100.
'''
Output:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

Explanation:
Print all numbers between 1 and 100 that have exactly two factors.
'''
#
'''
num=2
while num<=100:
        i=2
        while i<=num//2:
                if num%i==0:
                        break
                i+=1
        else:
                print(num,end=" ")
        num+=1
        
'''

#5. Write a Python program using a while loop to check whether a given number is a palindrome or not.
'''
Input:121
Output:Palindrome Number

Input:123
Output:Not a Palindrome Number

Explanation:
A palindrome number remains the same when reversed.

'''
#
'''
n=int(input("enter:"))
i=n
pal=0
while n>0:
        dig=n%10
        pal=pal*10+dig
        n=n//10
if i==pal:
        print("palindrome")
else:
        print("not palidrome")
'''
#6. Write a Python program using a while loop to reverse a given number.
'''
Input:1234
Output:4321

Explanation:
Extract each digit and construct the reversed number.
'''
#
'''
n=int(input("enter:"))
rev=0
while n>0:
        dig=n%10
        rev=rev*10+dig
        n//=10
print(rev)

'''
#7. Write a Python program using a while loop to count the number of digits in a given number.
'''
Input:56789

Output:5

Explanation:
The number contains 5 digits
'''
#
'''
n=int(input("enter:"))
cnt=0
while n>0:
        cnt=cnt+1
        n//=10
print(cnt)
 '''
#8. Write a Python program using a while loop to find the sum of digits of a given number.
'''
Input:345
Output:12

Explanation:
3 + 4 + 5 = 12
'''
#
'''
n=int(input("enter:"))
sum=0
while n>0:
    dig=n%10
    sum=sum+dig
    n//=10
print(sum)

'''
#9.Write a Python program using a while loop to calculate the factorial of a given number.
'''
Input:5
Output:120

Explanation:
5 × 4 × 3 × 2 × 1 = 120
'''
n=int(input("enter:"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i+=1
print(fact)   









