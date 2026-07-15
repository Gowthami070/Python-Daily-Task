#1.Write a Python program to print all numbers in a list whose reverse is a perfect square.
'''
Input:
[12, 31, 61, 52, 94]
Output:
[61]
Explanation:
Reverse of 61 is 16, which is a perfect square.
'''
#2.Write a Python program to print all numbers in a list whose product of digits is greater than the sum of digits.
'''
Input:
[12, 23, 34, 51, 22]
Output:
[23,34]
Explanation:
23 → Product = 6, Sum = 5
34 → Product = 12, Sum = 7
'''
#
'''
x=[12, 23, 34, 51, 22]
y=[]
for i in x:
    sum=0
    if i>0:
        dig=i%10
        product=dig*i
        sum=product+sum
        i=i//10
if product>sum:
        y.append(product)
print(i)
  '''      
##3.Write a Python program to print all numbers in a list whose square ends with the same digit as the original number.
'''
Input:
[5, 6, 7, 10, 25]
Output:
[5,6,10,25]
'''
#
'''
x=[5, 6, 7, 10, 25]
z=[]
for i in x:
        y=i**2
        dig=y%10
        lst=i%10 
        if lst==dig:
            z.append(i)
print(z)
'''
#4.Write a Python program to print all unique elements in a list.
'''
Input:
[10, 20, 10, 30, 20, 40, 50, 40]
Output:
[30, 50]
'''
#
'''
x=[10, 20, 10, 30, 20, 40, 50, 40]
y=[]
for i in x:
    z.count(i)
    if z>=2:
        z.remove()
    y.append(i)
print(y)
 '''   
#5.Write a Python program to reverse every element in a list.
'''
Input:
[123, 405, 78]
Output:
[321, 504, 87]
'''
#
x=[123, 405, 78]
y=[]
for i in x:
    rev=0
    while i>0:
        dig=i%10
        rev=rev*10+dig
        i=i//10
    y.append(rev)
print(y)
    
  
