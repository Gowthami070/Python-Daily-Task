#1.Write a Python program to find the union of two sets and display the result?
'''
Sample Input:
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
Sample Output:{10, 20, 30, 40, 50, 60}
'''
#
'''
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
c=A.union(B)
print(c)
'''
#2. Write a Python program to find the intersection of two sets?
'''
Sample Input:
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
Sample Output:{30, 40}
'''
#
'''
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
c=A.intersection(B)
print(c)
'''
#3. Write a Python program to find the difference between two sets (A - B)?
'''
Sample Input:
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
Sample Output:{10, 20}
'''
#
'''
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
c=A.difference(B)
print(c)
'''
#4.Write a Python program to merge a list and a tuple into a single list?
'''
Sample Input:
List  = [10, 20, 30]
Tuple = (40, 50, 60)

Sample Output:[10, 20, 30, 40, 50, 60]
'''
#
'''
List  = [10, 20, 30]
Tuple = (40, 50, 60)
c=tuple(List)+Tuple
print(c)
'''
#5.Write a Python program to find the largest element in a tuple and the smallest element in a list?
'''
Sample Input:
List  = [15, 8, 30, 12]
Tuple = (45, 10, 60, 25)

Sample Output:
Largest in Tuple = 60
Smallest in List = 8
'''
#
'''
List  = [15, 8, 30, 12]
Tuple = (45, 10, 60, 25)
a=max(Tuple)
b=min(List)
print("Largest in Tuple=",a)
print("Smallest in List=",b)
'''
#6. Write a Python program to find the first repeated element in a tuple?
'''
Sample Input:(10, 20, 30, 20, 40, 50)
Sample Output:20
'''
#
'''
x=(10, 20, 30, 20, 40, 50)
y=list(x)
z=[]
for i in y:
    if i in z:
        z.append(i)
print(z)
'''
#7.Write a Python program to count how many elements in a tuple are greater than the average of all elements?
'''
Sample Input:(10, 20, 30, 40, 50)
Sample Output:2
'''
#
'''
x=(10, 20, 30, 40, 50)
avg=sum(x)/len(x)
cnt=0
for i in x:
    if i>avg:
        cnt=cnt+1
print(cnt)
'''
#8.Write a Python program to find the first pair of adjacent elements whose sum is a prime number.
'''
Sample Input:(4, 7, 6, 5, 8)
Sample Output:6 5
'''
#
