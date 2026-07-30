#1.Write a Python program using a lambda function to find the square of a given number.
'''
Input:5
Output:25
'''
#
'''
y=lambda num:num**2
res=y(5)
print(res)
'''
#2. Write a Python program using a lambda function to check whether a given number is even or odd.
'''
Input:8
Output: Even
'''
#
'''
y=lambda n:'Even' if n%2==0 else 'odd'
res=y(5)
print(res)
'''
#3. Write a Python program using a lambda function to find the larger of two given numbers.
'''
Input:10 25
Output:25
'''
#
'''
z=lambda x,y: x if x>y else y
res=z(15,13)
print(res)
'''
#4. Write a Python program using a lambda function to multiply two given numbers.
'''
Input:6 7
Output:42
'''
#
'''
z=lambda x,y: x*y
res=z(6,7)
print(res)
'''
#5.Write a Python program to create a decorator that adds 18% tax to the price returned by a function.
'''
Input:1000
Output:1180
'''
#
'''
def tax(fun):
    def innerfun(n):
        taxs=n*(18/100)
        return taxs
    return innerfun
@tax
def fun1(n):
    return n
n=int(input("Enter:"))
res=fun1(n)
print("Total price=",res+n)
'''
#6.Write a Python program to create a decorator that prints the execution time of a function.
'''
Input:5
Output: Execution Time: 0.002 seconds
'''
#
'''
import time

def timecal(fun):
    def innerfun(n):
        start = time.time()
        result = fun(n)
        end = time.time()
        print(f"Execution Time: {end-start:.6f} seconds")
        return result
    return innerfun

@timecal
def fun1(n):
    return n

n = int(input("Enter: "))
print(fun1(n))
'''
