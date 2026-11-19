# 1. Write a program to find area and perimeters of circle, rectangle, square.
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

