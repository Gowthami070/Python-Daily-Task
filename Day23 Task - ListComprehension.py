#1.Write a Python program using list comprehension to replace all negative numbers in a list with 0?
'''
Sample Input:[10, -5, 20, -8, 15]
Sample Output:[10, 0, 20, 0, 15]
'''
#
'''
x=[10, -5, 20, -8, 15]
y=[0 if i<0  else i for i in x]
print(y)
'''
#2.Write a Python program using list comprehension to create a list of tuples where each tuple contains a number and its cube?
'''
Sample Input:[1, 2, 3, 4]
Sample Output:[(1, 1), (2, 8), (3, 27), (4, 64)]
'''
#
'''
x=[1, 2, 3, 4]
y=[(i,(i**3)) for i in x]
print(y)
'''
#3.Write a Python program to find the product that generated the highest revenue?
'''
Sample Input:
Price = {'Pen':10,'Book':50,'Bag':500}
Sold  = {'Pen':20,'Book':5,'Bag':2}
Sample Output:Bag
'''
#
'''
price = {'Pen':10,'Book':50,'Bag':500}
sold  = {'Pen':20,'Book':5,'Bag':2}
max_p=''
max_r=0
for i in price:
    revenue=price[i]*sold[i]
    if revenue>max_r:
        max_r=revenue
        max_p=i
print(max_p)
  '''      
#4.Write a Python program to merge two dictionaries. If the same key exists in both dictionaries, add their values?
'''
Sample Input:
D1 = {'A':10,'B':20,'C':30}
D2 = {'B':15,'C':5,'D':40}
Sample Output:{'A':10,'B':35,'C':35,'D':40}
'''
#
'''
D1 = {'A':10,'B':20,'C':30}
D2 = {'B':15,'C':5,'D':40}
result = {}
for i in D1:
    result[i] = D1[i]
for i in D2:
    if i in result:
        result[i] = result[i] + D2[i]
    else:
        result[i] = D2[i]
print(result)
'''
#5.Write a Python program to invert a dictionary where duplicate values should be stored as a list of keys?
'''
Sample Input:{'A':1,'B':2,'C':1,'D':3}
Sample Output:{1:['A','C'],2:['B'],3:['D']}
'''
x={'A':1,'B':2,'C':1,'D':3}
y={}
for i in x:
    values=x[i]
    if values in y:
        y[values].append(i)
    else:
        y[values]=[i]
print(y)


























