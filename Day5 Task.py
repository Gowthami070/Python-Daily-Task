#1.Write a Python program to repeatedly subtract 3 from a number until the result becomes less than 0?
'''
Input:14
Output:14 11 8 5 2

Explanation:
Stop the loop before printing a negative value.
'''
#9
'''
num = int(input("Enter: "))
while True:
    if num < 0:
        break
    print(num, end=" ")
    num -= 3
'''
#2.Write a Python program to repeatedly double a number until it exceeds 100?
'''
Input:3
Output:3 6 12 24 48 96

Explanation:
Terminate the loop when the next value becomes greater than 100.
 '''
#
'''
n=int(input("enter:"))
while True:
    if n>100:
        break
    print(n,end=" ")
    n=n*2
'''
#3.Write a Python program to count how many times a number can be divided by 2 before it becomes odd?
'''
Input:40
Output:3

Explanation:
40 → 20 → 10 → 5
The number was divided by 2 three times.
'''
#
'''
n=int(input("enter:"))
cnt=0
while n%2==0:
    n=n//2
    cnt+=1
print(cnt)
'''
#4.Write a Python program to find the first even number greater than n that is divisible by 7 using a while loop and break.
'''
Input:40
Output:42

Explanation:
Terminate the loop immediately after finding the required number.
'''
#
'''
n=int(input("Enter:"))
while n%2==0 and n%7==0 and n>0:
    break
print(n)
n+=1
 '''       
#5.Write a Python program to find the first number greater than n that is divisible by 9 but not by 3 using a while loop and break.
'''
Input:50

Output:No such number
Explanation:
Every number divisible by 9 is also divisible by 3
'''
n1=int(input("enter:"))
n2=int(input("enter:"))
cnt=0
cnt1=0
for i in range(n1,n2+1):
    temp=i
    while temp>0:
        dig=temp%10
        if dig%2==0:
            cnt+=1
        else:
            cnt1+=1
        temp=temp//10
print(cnt)
print(cnt1)

        




