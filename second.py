#  Write a program to find area and perimeters of circle, rectangle, square.
# circle
r=float(input("enter a  circle radius:"))
circle_area=3.14*r*r
circle_perimeter=2*3.14*r
print(f' The Area of circle is {circle_area} and the perimeter of circle is {circle_perimeter}')

# rectangle
l=int(input("enter a rectangle length:"))
b=int(input("enter a rectangle breadth:"))
rectangle_area=l*b
rectangle_perimeter=2*(l+b)
print(f' The are of rectangle is {rectangle_area} and the perimeter of recatngle is {rectangle_perimeter}')

# square
s=int(input("enter a square side:"))
square_area=s*s
square_perimeter=4*s
print(f' the are of square is{square_area} and the perimeter of square is{square_perimeter}')

# Write a program to check whether given sides form a triangle or not: logic sum of any two sides must be greater than third side.
a=int(input("enter first side: "))
b=int(input("enter second side: "))
c=int(input("enter third side: "))
if a + b > c and a + c > b and  b + c > a:
    print("it is a valid traingle")
else:
    print("it is an invalid traingle")
    
# write a program to check in which quadrant does the given coordinates falls:
x=int(input(" enter x coordinate:"))
y=int(input(" enter y coordinate:"))
if x > 0 and y > 0:
    print("the point lies in first quadrant")
elif x < 0 and y > 0:
    print("the point lies in second quadrant")
elif x < 0 and y < 0:
    print("the point lies in third quadrant")
elif x > 0 and y < 0:
    print("the point lies in fourth quadrant")



