#1.Exam Score Calculation
'''
A student receives marks for 5 subjects one by one.
Write a Python program using a while loop to calculate the total marks and average.

Input:80 75 90 85 70
Output:
Total = 400
Average = 80
'''
n=int(input("Enter:"))
total=0
count=0
while n>0:
    total=total+n
    count=count+1
    print("Total =",total)
'''
average=total/count
print("Average =",average)
 '''   
#3.Write a Python program using a while loop to count how many numbers must be added starting from 1 until the sum becomes greater than N?
'''
Input:20
Output:6
Explanation:1 + 2 + 3 + 4 + 5 + 6 = 21
'''
#
'''
n=int(input("Enter:"))
cnt=0
i=1
sum=0
while i<=n:
        sum=sum+i
        cnt=cnt+1
        if sum>n:
            break
        i=i+1
print(cnt)
'''
#4.Write a Python program using a while loop to check whether a given number is a palindrome or not. If the number is a palindrome, determine whether it is even or odd?
'''
Input:1221
Output:
Palindrome Number
Even
'''
#
'''
n=int(input("Enter:"))
pal=0
bkp=n
while n>0:
    dig=n%10
    pal=pal*10+dig
    n=n//10
print(pal)
if pal==bkp:
    print("palindrome")
    if pal%2==0:
        print("Even")
    else:
        print("Odd")
else:
    print("Not a palidrome")
'''
#5.Write a Python program using a while loop to find the smallest number greater than N whose sum of digits is equal to 10?
'''
Input:25
Output:28

Explanation:
The numbers greater than 25 are:
26 → 2 + 6 = 8
27 → 2 + 7 = 9
28 → 2 + 8 = 10 ✓
Therefore, 28 is the smallest number greater than 25 whose digit sum is 10.
'''
#
'''
n=int(input("enter:"))
i=n+1
while True:
    temp=i
    sum=0
    while temp>0:
        dig=temp%10
        sum=sum+dig
        temp=temp//10
    if sum==10:
        print(i)
        break
    i+=1
'''

