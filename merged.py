def merge(L1, L2):
    sorted = True
    NL = L1+L2

    while sorted :
        sorted = False
        for n in range(len(NL) -1 ):
            if NL[n] > NL[n+1]:
                NL[n] , NL[n +1] = NL[n+1],NL[n]
                sorted = True
    return NL

def main():
    pass

if __name__ == "__main__":
    main()
