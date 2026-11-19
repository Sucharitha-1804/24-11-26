#write a program to check whether given sides from atriangle or not: logic sum of any two sides must be greater than third side..
a=int(input("enter first side: "))
b=int(input("enter second side: "))
c=int(input("enter third side: "))
if a + b > c and a + c > b and  b + c > a:
    print("it is a valid traingle")
else:
    print("it is an invalid traingle")