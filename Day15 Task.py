#1.Write a Python program to reverse a list without using any built-in functions like reverse() or slicing.?
'''
   input: list: [10, 20, 30, 40, 50]
   Output: list: [50, 40, 30, 20, 10]
'''
#
'''
x=[10, 20, 30, 40, 50]
s=0
e=len(x)-1
while s<e:
    x[s],x[e]=x[e],x[s]
    s=s+1
    e=e-1
print(x)
'''
#2.Write a Python program to concatenate two lists without using the built-in extend() method.?
'''
 Input:a = [1, 2, 3]
           b = [4, 5, 6]
           '''
#
'''
a = [1, 2, 3]
b = [4, 5, 6]
c=a+b
print(c)
'''
#3.Write a Python program to insert an element at a specific index in a list.?
'''
  Input:lst = [1, 2, 4]
           index = 2
          value = 3
  output:[1, 2, 3, 4]
  '''
#
'''
x=[1, 2, 4]
x.insert(2,3)
print(x)
'''

#4.Write a Python program to rotate a list to the left by k positions?
'''
      input:lst = [1, 2, 3, 4, 5]
                k = 2 
      output:Rotated List: [3, 4, 5, 1, 2]
'''
#
'''
lst = [1, 2, 3, 4, 5]
r_type=input("Enter the type RR/LR:")
k=int(input("Enter the k value:"))
#k=k%len(k)
for i in range(0,k):
    if r_type=='RR':
        y=lst.append(lst.pop(0))
        print(lst)
    elif r_type=='LR':
        y=lst.insert(0,pop())
        print(lst)
    else:
        print("Choose the correct option")
  '''  
#5.Write a Python program to find the index of a specific element in a given list?
'''
input:
my_list = [10, 20, 30, 40, 50]
element = 30
output:The index of 30 is: 2
'''
#
'''
my_list = [10, 20, 30, 40, 50]
n=int(input("Enter:"))
if n in my_list:
    print("The index of",n ,"is:", my_list.index(n))
'''
