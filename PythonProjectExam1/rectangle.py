import math

#calculate the area of a rectangle given its length and width prompted by the user
#custom function to calculate the area, use F-Strings to display area


def rectangle(length, width):
    return length * width
width = float(input("Enter the width of a rectangle: "))
length = float(input("Enter the length of a rectangle: "))
area = rectangle(length, width)
print(f"The area of the rectangle is {rectangle(length, width):.2f}")

