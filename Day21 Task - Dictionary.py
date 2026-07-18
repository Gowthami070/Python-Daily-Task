#1. Write a Python program to create a dictionary containing student names as keys and their marks as values. Display all the key-value pairs?
'''
Sample Input:{'Ravi': 85, 'Priya': 92, 'John': 78}
Sample Output:
Ravi : 85
Priya : 92
John : 78
'''
#
'''
student={'Ravi' : 85,'Priya ': 92,'John' : 78}
for i in student:
    print(i,':',student[i])
'''
#2. Write a Python program to find the student who scored the highest marks in a dictionary?
'''
Sample Input:{'Ravi': 85, 'Priya': 92, 'John': 78}
Sample Output:
Priya
'''
#
'''
student={'Ravi': 85, 'Priya': 92, 'John': 78}
c=max(student.values())
for i in student:
    if student[i]==c:
        print(i)
'''
#3. Write a Python program to count the total number of key-value pairs in a dictionary?
'''
Sample Input:{'A': 10, 'B': 20, 'C': 30, 'D': 40}
Sample Output:
'''
#
'''
number={'A': 10, 'B': 20, 'C': 30, 'D': 40}
cnt=0
for i in number:
    if i in number:
        cnt=cnt+1
print(cnt)
'''
#4. Write a Python program to calculate the sum of all values in a dictionary?
'''
Sample Input:{'Math': 90, 'Science': 85, 'English': 80}
Sample Output:255
'''
#
'''
marks={'Math': 90, 'Science': 85, 'English': 80}
c=marks.values()
print(sum(c))
'''
#5. Write a Python program to count how many values in a dictionary are even numbers?
'''
Sample Input:{'A': 10, 'B': 15, 'C': 20, 'D': 25}
Sample Output:2
'''
#
'''
numbers={'A': 10, 'B': 15, 'C': 20, 'D': 25}
even_cnt=0
for i in numbers.values():
    if i%2==0:
        even_cnt+=1
print(even_cnt)
'''
#6.Write a Python program to find the largest number obtained by removing exactly one occurrence of the digit 5 from a given number?
'''
If the given number does not contain the digit 5, print -1.

Sample Input 1:

text
53215


*Sample Output 1:*

text
5321


*Explanation:*

* Remove the first 5 → 3215
* Remove the second 5 → 5321
* Compare both results.
* The largest number is *5321*.

---

*Sample Input 2:*

text
15958


*Sample Output 2:*

text
1958


*Explanation:*

* Remove the first 5 → 1958
* Remove the second 5 → 1598
* The largest number is *1958*.

---

*Sample Input 3:*

text
4


*Sample Output 3:*

text
-1


*Explanation:*
The number does not contain the digit 5, so the output is *-1*.
'''
#
'''
n = input()
if '5' not in n:
    print(-1)
else:
    large = 0
    for i in range(len(n)):
        if n[i] == '5':
            num = int(n[:i] + n[i+1:])
            if num > large:
                large = num
    print(large)
'''
