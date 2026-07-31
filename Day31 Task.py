#1.Reverse Until Palindrome
'''
Write a Python program to create a function that repeatedly reverses and adds a number until it becomes a palindrome.
Sample Input: 56
Sample Output: 56 + 65 = 121
Palindrome Found
'''
#
'''
def ispalidrome(number):
    sum=0
    pal=1
    while True:
        if number>0:
            number=number%10
            pal=pal*10+number
            sum=sum+pal
            number=number//10
    if sum==number:
        return 'palidrome'
number=int(input("Enter:"))
print(ispalidrome(number))
'''
#2. Equal Frequency
'''
Write a Python program to create a function that checks whether all characters in a string occur the same number of times.
Sample Input: aabbcc
Sample Output: Equal Frequency
'''

#3. Alternate Prime Numbers
'''
Write a Python program to create a function that prints every alternate prime number from a list.
Sample Input: [2,3,5,7,11,13,17]
Sample Output: 2 5 11 17
'''
#
'''
def is_prime(n):
    if n<2:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
def alternate_prime(nums):
    primes=[]
    for i in nums:
        if is_prime(i):
            primes.append(i)
    for i in range(0,len(primes),2):
        print(primes[i],end=' ')
nums=[2,3,5,7,11,13,17]
alternate_prime(nums)
'''
#4.Remove Every Third Element
'''
Write a Python program to create a function that removes every third element from a list?

Sample Input:[10, 20, 30, 40, 50, 60, 70]
Sample Output:[10, 20, 40, 50, 70]
'''
#
'''
def remove_third(nums):
    result=[]
    for i in range(len(nums)):
        if (i+1)%3!=0:
            result.append(nums[i])
    return result
nums=[10, 20, 30, 40, 50, 60, 70]
print(remove_third(nums))
'''
#5.Smart Locker System
'''
Write a Python program to  create a function Locker.
Implement methods to:
Lock the locker.
Unlock using a PIN.
Count the number of wrong PIN attempts.
Block the locker after 3 incorrect attempts.
'''
