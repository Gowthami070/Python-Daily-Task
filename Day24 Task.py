#1.Write a Python program to find the longest word stored as a dictionary value?
'''
Sample Input:{1:'Python',2:'Programming',3:'Code'}
Sample Output:Programming
'''
#
'''
x = {1: 'Python', 2: 'Programming', 3: 'Code'}
longest = ""
for i in x.values():
    if len(i)>len(longest):
        longest = i
print(longest)
'''
#2.Write a Python program to group student names by their grades?
'''
Sample Input:{'Ram':'A','Sam':'B','John':'A','Tom':'C'}
Sample Output:{'A':['Ram','John'],'B':['Sam'],'C':['Tom']}
'''
#
'''
x={'Ram':'A','Sam':'B','John':'A','Tom':'C'}
y={}
for i in x:
    values=x[i]
    if values in y:
        y[values].append(i)
    else:
        y[values]=[i]
print(y)
'''
#3.Write a Python program to find the product that is out of stock?
'''
Sample Input:{'Pen':20,'Book':0,'Bag':5,'Bottle':0}
Sample Output:
Book
Bottle
'''
#
'''
x={'Pen':20,'Book':0,'Bag':5,'Bottle':0}
y=[]
for i in x:
    values=x[i]
    if values==0:
        y.append(i)
print(y)
'''
#4.Task 1: Student Performance Analysis
'''
Create a dictionary where the key is the student name and the value is a list of marks in three subjects?
Perform the following operations:
Calculate the total marks of each student.
Calculate the average marks of each student.
Print the topper's name.
Print the names of students whose average is greater than 75.
Sample Input:
{
'Rahul': [85, 90, 78],
'Priya': [92, 88, 95],
'Arun': [70, 65, 72],
'Neha': [80, 76, 84]
}
Sample Output:
Rahul -> Total: 253, Average: 84.33
Priya -> Total: 275, Average: 91.67
Arun -> Total: 207, Average: 69.00
Neha -> Total: 240, Average: 80.00

Topper: Priya
Students with Average > 75:
Rahul
Priya
Neha
'''
#

student={
    'Rahul':[85, 90, 78],
    'Priya': [92, 88, 95],
    'Arun': [70, 65, 72],
    'Neha': [80, 76, 84]
}
sumlist=[]
avglist=[]
first=0
for i in student.values():
        tsum=sum(i)
        avg=tsum/len(i)
        sumlist.append(tsum)
        avglist.append(avg)
        if avg>75:
             print(i)
for j in sumlist:
    if j>first:
        first=j
print("Toppers:",first)

print("Total marks:",sumlist)
print("Average:",avglist)

#print(student.keys(),'=','Total:',sumlist,'Average:',avglist)  

