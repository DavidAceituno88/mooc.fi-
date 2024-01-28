#!/usr/bin/env python3

import math


def main():
    n = True
    while n == True:
        shape = input("Choose a shape (triangle,rectangle,circle): ")
        if shape == "triangle":
            n = True
            base= float(input("Give base of triangle:"))
            height = float(input("Give height of triangle:"))
            area = (height*base)/2
            print("The area is ",area)
        elif shape == "circle":
            n = True
            radius = float(input("Give radius of circle:"))
            area = math.pi*(radius**2)
            print("The area is ",area)
        elif shape == "rectangle":
            n = True
            height = float(input("Give height of the rectangle:"))
            width = float(input("Give width of the rectangle:"))
            area = (height*width)
            print("The area is ",area)
        elif shape == '':
            n=False
        else:
            n=True
            print("Unknown shape!")

    # enter you solution here

if __name__ == "__main__":
    main()
