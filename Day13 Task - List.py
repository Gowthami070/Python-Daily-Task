#1.Write a Python program to separate the even and odd elements of a list into two different lists?
'''
Sample Input: 10 15 22 33 40 55
Sample Output:
Even List: 10 22 40
Odd List: 15 33 55
'''
'''
x=[10,15, 22, 33, 40,55]
even_list=[]
odd_list=[]
for i in x:
    i=int(input())
    if i%2==0:
        x=x.append(even_list)
        print("Even List:",x)
    else:
        x=x.append(odd_list)
        print("Odd List:",x)
        '''

#2.Write a Python program to count the total number of prime numbers present in a list?
'''
Sample Input:[2 4 5 9 11 15]
Sample Output:3
'''
#

x=[2,4,5,9,11,15]
k=2
i=1
cnt=0
for j in x:
    while i<=j:
        if j%i==0:
            break
        else:
            cnt=cnt+1
            if cnt==k:
                print("The prime numbers")
        print(cnt)
    i=i+1
    

#3.Write a Python program to move all zero elements to the end of a list while maintaining the order of the remaining elements?
'''
Sample Input:[2 0 5 0 8 1 0]
Sample Output:[2 5 8 1 0 0 0]
'''
#
'''
x=[2,0,5,0 ,8 ,1, 0]
for i in x:
    if i==0:
        x.remove(i)
        x.append(i)
    print(x)
 '''       

#4.Write a Python program to find the missing number in a list?
'''
Sample Input:[1 2 4 5]
Sample Output:3
'''
#
'''
x=[1,2,4,5]
for i in range(min(x),max(x)):
    if i not in x:
        print(i)
    '''
#5.Write a Python program to rotate the elements of a list one position to the left?
'''
Sample Input:[10 20 30 40 50]
Sample Output:[20 30 40 50 10]
'''
#
'''
x=[10,20,30,40,50]
r_type=input("enter the type you want RR/LR:")
k=int(input("Enter the number:"))
k=k%len(x)
for i in range(0,k):
    if r_type=='RR':
        x.append(x.pop(0))
        print(x)
    elif r_type=='LR':
        x.insert(0,x.pop())
        print(x)
    else:
        print("Choose the correct option")
'''      
            
