#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    root = (b**2)-(4*a*c)
          
    pos = ((-b + math.sqrt(root))/(2*a))
    neg = ((-b - math.sqrt(root))/(2*a))
    
    return (pos,neg)


def main():
    print(solve_quadratic(1,-3,2))
    print(solve_quadratic(1,2,1))
    pass

if __name__ == "__main__":
    main()
