#!/usr/bin/env python3

def triple(t):
    return t*3

def square(t):
    return t**2


def main():
    
    for n in range(1,11):
        a = triple(n)
        b = square(n)
        if(b <= a):
            print(f"triple({n})=={a} square({n})=={b}")
        else:
            
            break
            
    pass

if __name__ == "__main__":
    main()
