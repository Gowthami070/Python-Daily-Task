#1.Write a Python program to count the number of even and odd elements in a list.
'''
Input:
[10, 15, 20, 25, 30, 35]
Output:
Even Count = 3
Odd Count = 3
'''
#
'''
x=[10, 15, 20, 25, 30, 35]
even_cnt=0
odd_cnt=0
for i in x:
    if i%2==0:
        even_cnt=even_cnt+1
    else:
        odd_cnt=odd_cnt+1
print("Even count =",even_cnt)
print("Odd count =",odd_cnt)
'''
#2.Write a Python program to find the largest element in a list.
'''
Input:
[12, 45, 7, 89, 23]
Output:
89
'''
#
'''
x=[12, 45, 7, 89, 23]
print(max(x))
'''
#3.Write a Python program to count the number of prime numbers in a list.
'''
Input:
[2, 4, 5, 7, 8, 11, 15]
Output:
4
'''
#
x=[2, 4, 5, 7, 8, 11, 15]
for i in x:
    count=0
    while  
#4.Write a Python program to find the sum of all elements in a list.
'''
Input:
[10, 20, 30, 40]
Output:
100
'''
#
'''
x=[10, 20, 30, 40]
sum=0
for i in x:
    if i>0:
        sum=sum+i
print(sum)
'''
#5.Write a Python program to count how many numbers in a list are divisible by 3.
'''
Input:
[3, 5, 6, 9, 10, 12, 15]
Output:
5
'''
#
'''
x=[3, 5, 6, 9, 10, 12, 15]
count=0
for i in x:
    if i%3==0:
        count=count+1
print(count)
'''
#6.Write a Python program to find all palindrome numbers in a list.
'''
Input:
[121, 123, 454, 567, 787]
Output: 121 454 787
'''
#
'''
x=[121, 123, 454, 567, 787]
y=[]
for i in x:
    pal=0
    temp=i
    while i>0:
        dig=i%10
        pal=pal*10+dig
        i=i//10
    if temp==pal:
        y.append(temp)
print(y)
'''
