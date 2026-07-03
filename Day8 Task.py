#1.Write a Python program using a while loop to find the product of all non zero digits in a number and determine whether the product is a prime number or not?
'''
Input:20354
Output:
Product = 120
Not Prime

Explanation:
Non zero digits are 2, 3, 5, and 4.
Product = 2 × 3 × 5 × 4 = 120
Since 120 has factors other than 1 and itself, it is not a prime number.
'''
#
'''
n=int(input("enter:"))#20354
pr=1
while n>0:#20354>0-t
        dig=n%10#20354%10=4
        if dig!=0:#4!=0-t   
            pr=pr*dig#1*4=4
        n=n//10#20354
print(pr)
i=2
cnt=1
if pr%i==0:
        cnt=cnt+1
        if cnt<2:
                print("Prime")
        else:
                print("Not Prime")
'''
#2.Write a Python program using a while loop to count the number of prime digits in a given number?
'''
Input:237458
Output:4

Explanation:
Prime digits are 2, 3, 7, and 5.
 '''
'''n=int(input("enter:"))
cnt=0
i=2
while n>0:
        dig=n%10
        if dig%i==0:
                cnt=cnt+1
        n=n//10
if cnt>2:
        print(cnt)'''
#
'''
n=237458
c=0
while(n>0):
        d=2
        rem=n%10
        while(d<=rem//2):
                if(rem%d==0):
                        break
                d=d+1
        else:
                c=c+1
        n=n//10
print(c)
'''
#3.Write a Python program using a while loop to determine whether a number is a Spy Number?
'''
Input:123
Output:Spy Number

Explanation:
Sum of digits = 6
Product of digits = 6
Since both are equal, the number is a Spy Number.
'''
#
'''
n=int(input("enter:"))
sum=0
pr=1
while n>0:
      dig=n%10
      sum=sum+dig
      pr=pr*dig
      n//=10
#print(sum)
#print(pr)
if pr==sum:
        print("Its a Spy number")
else:
        print("Not a spy number")
'''
 
#4.Write a Python program using a while loop to find the difference between the largest digit and the smallest digit in a number?
'''
Input:947235
Output:7

Explanation:
Largest digit = 9
Smallest digit = 2
Difference = 7
'''
#
'''
n=int(input("enter:"))
large=0
small=9
while n>0:
        dig=n%10
        if dig>large:
                large=dig
        if dig<small:
                small=dig
        n=n//10
print(large-small)

'''
#5.Write a Python program using a while loop to find the Nth prime number?
'''
Input:5
Output:11

Explanation:
Prime numbers are:
2, 3, 5, 7, 11, ...
The 5th prime number is 11.
'''
#
'''
n=int(input("Enter:"))
num=2
cnt=0
while True:
        i=2
        while i<=num//2:
                if num%i==0:
                        break
                i+=1
        else:
                cnt+=1
                if cnt==n:
                        print(num)
                        break
        num+=1
'''
#6.Write a Python program using a while loop to check whether a number contains consecutive repeated digits?
'''
Input:122345
Output:Consecutive Digits Found

Explanation:
The digit 2 appears consecutively.
'''

n=int(input("enter:"))
d=0
while n>0:
        dig=n%10
        if d==dig:
                print(d)
                print("Print consecutive digits found")
                break
        d=dig
        n=n//10
        
















        
