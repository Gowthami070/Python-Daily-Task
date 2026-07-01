#1.Write a Python program using a while loop to find the smallest number greater than n whose last digit is 7?
'''
Input:25
Output:27

Explanation:
Continue checking numbers until a number ending with 7 is found
'''
#
'''
n=int(input("enter:"))
i=n+1
while True:
    if i%10==7:
       print(i)
       break
    i+=1
  '''
#2.Write a Python program using a while loop to find the sum of all numbers between 1 and n whose last digit is an odd number.
'''
Input:15
Output:64

Explanation:
1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 = 64
'''
#
'''
n=int(input("enter:"))
i=1
sum=0
while i<=n:
    if i%2!=0:
        sum=sum+i
    i+=1
print(sum)
  '''
#3.Write a Python program using a while loop to repeatedly add the digits of a number until a single digit is obtained?
'''
Input:9875
Output:2

Explanation:
9 + 8 + 7 + 5 = 29
2 + 9 = 11
1 + 1 = 2
'''
#
'''
n=int(input("enter:"))
while True:
    s=0
    while n>0:
        dig=n%10
        s=s+dig
        n=n//10
    if s>9:
        n=s
    else:
        print(s)
        break
'''
#4.Write a Python program using a while loop to determine how many times a number can be divided by 2 before it becomes odd?
'''
Input:48
Output:4

Explanation:48 → 24 → 12 → 6 → 3
The number can be divided by 2 four times.
'''
#
'''
n=int(input("Enter:"))
cnt=0
while n%2==0:
    n=n//2
    cnt+=1
print(cnt)

'''
#5.Write a Python program using a while loop to find the largest digit in a number without converting the number into a string.
'''
Input:583921
Output:9

Explanation:
Extract each digit and keep track of the maximum dig
'''
#
'''
n=int(input("enter:"))
num=0
while n>0:#583921
    dig=n%10#0%10-0
    if dig>num:#9>5
        num=dig*1#9*1=9
    n=n//10#5//10-0
print(num)#9
'''















