# 1. write a program to print numbers  1 to 20 using a for loop.
'''for i in range(1,21):
      print(i)'''
      
#Write a program to find the sum of all even numbers from 1 to 50
'''total=0
for i in range(1,51):
    if i%2==0:
        total=total+i
print("sum of even numbers:",total)'''

#Write a program to print the multiplication table of a number entered by the user.
'''number=int(input("enter a number:"))
for i in range(1,11):
    print(number, "x",i,"=",number *i)'''
    
#Write a program to count how many positive numbers are present in a list
'''numbers=[10,-5,20,-8,30,0]
count=0
for i in numbers:
    if i >0:
        count=count+ 1
print("positive numbers count:",count)'''

#Write a program to calculate the sum of all numeric digits present in a string
'''name="abc12de34"
total=0
for i in name:
    if i.isdigit():
        total=total +int(i)
print("sum of digits:",total)'''

#Write a program to print numbers from 10 to 1 using a while loop.
'''i=10
while i>=1:
    print(i)
    i=i-1'''
    
#Write a program to calculate the sum of digits of a given number
'''number=int(input("enter a number:"))
total=0
while number >0:
    digit =number %10
    total=total+digit
    number=number//10
print("sum of digits:",total)'''

#Write a program to count the total number of digits in a given number.
'''number=int(input("enter a number:"))
count=0
while number > 0:
    number=number//10
    count=count +1
print("total number of digits:",count)'''

#Write a program to calculate the factorial of a number using a while loop.
'''number =int(input("enter a number:"))
fact=1
i=1
while i<=number:
    fact=fact *i
    i=i+1
print("factorial:",fact)'''

#Write a program to print all odd numbers between 1 and a number entered by the user.
number=int(input("enter a number:"))
for i in range(1, number+1):
    if i%2!=0:
        print(i)