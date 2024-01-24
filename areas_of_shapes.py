#!/usr/bin/env python3

import math


def main():
    n = False
    while n == True:
        shape = input("Choose a shape (triangle,rectangle,circle): ")
        if shape == "triangle":
            n = True
            base= float(input("Give base of triangle:"))
            height = float(input("Give height of triangle:"))
            area = (height*base)/2
            print(area)
        elif shape == "circle":
            n = True
            radius = float(input("Give radius of circle:"))
            area = (math.pi*radius)**2
            print(area)
        elif shape == '':
            n=False

    # enter you solution here

if __name__ == "__main__":
    main()
