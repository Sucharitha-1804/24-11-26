
#write a program to check in which quadrant does the given coordinates falls:
x=int(input(" enter x coordinate:"))
y=int(input(" enter y coordinate:"))
if x > 0 and y > 0:
    print("the pointlies in first quadrant")
elif x < 0 and y > 0:
    print("the point lies in second quadrant")
elif x < 0 and y < 0:
    print("the point lies in third quadrant")
elif x > 0 and y < 0:
    print("the point lies in fourth quadrant")
