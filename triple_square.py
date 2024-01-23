#!/usr/bin/env python3

def triple(t):
    return t*3

def square(t):
    return t**2


def main():
    
    for n in range(1,11):
        if(square(n) > triple(n)):
            break
        else:
            print("triple(",n,") == ",triple(n), "square(",n,") == ",square(n))
    pass

if __name__ == "__main__":
    main()
