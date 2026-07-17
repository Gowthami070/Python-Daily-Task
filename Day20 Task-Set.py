#1.Write a Python program to find the sum of all strong numbers present in a set?
'''
Sample Input:{145, 125, 2, 40585}
Sample Output:40732
'''
#
'''
x={145, 125, 2, 40585}
total=0
for i in x:
    sum=0
    j=i
    while j>0:
        dig=j%10
        fact=1
        while dig>=1:
            fact=fact*dig
            dig-=1
        sum=sum+fact
        j=j//10
    if sum==i:
        total=total+i
print(total)
  '''   
#2.Write a Python program to find the largest palindrome number in a set?
'''
Sample Input:{11, 22, 121, 88, 99}
Sample Output:121
'''
#
'''
x={11, 22, 121, 88, 99}
largest=0
for i in x:
    temp=i
    pal=0
    while temp>0:
        dig=temp%10
        pal=pal*10+dig
        temp=temp//10
    if pal==i:
        if i>largest:
            largest=i
print(largest)
'''
#3. Write a Python program to find the elements that are common to exactly two sets?
'''
Sample Input:
A = {10, 20, 30, 40}
B = {20, 30, 50, 60}
C = {30, 40, 60, 70}

Sample Output:{20, 40, 60}
'''
#
'''
A = {10, 20, 30, 40}
B = {20, 30, 50, 60}
C = {30, 40, 60, 70}
result=(A&B)|(B&C)|(C&A)
result=result-(A&B&C)
print(result)
  '''  
#4.Write a Python program to determine whether the union of two sets contains only prime numbers?
'''
Sample Input:
A = {2, 3, 5}
B = {7, 11, 13}
Sample Output:True
'''
#
'''
A = {2, 3, 5}
B = {7, 11, 13}
c=A.union(B)
flag=True
for i in c:
    if i<2:
        flag=False
        break
    for j in range(2,i):
        if i%j==0:
            flag=False
            break
    if flag==False:
            break
print(flag)
 '''  
#5. Write a Python program to find the sum of all perfect numbers present in the intersection of two sets?
'''
Sample Input:
A = {6, 12, 28, 496}
B = {6, 28, 30, 496}

Sample Output:530
'''
#
'''
A = {6, 12, 28, 496}
B = {6, 28, 30, 496}
c=A.intersection(B)
total=0
for i in c:
    j=1
    sum=0
    while j<i:
        if i%j==0:
            sum=sum+j
        j=j+1
    if sum==i:
        total=total+i
print(total)
'''
