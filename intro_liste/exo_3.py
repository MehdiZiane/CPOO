def main():
    L = [987, 65, 43, 21, 43, 98, 145]
    print(L)
    compteur = 0 
    for i in L:
        if i == 43:
            compteur +=1
    print(compteur)
    L.append(45)
    print(len(L))
    del L[2]
    print(L)
    L.reverse()
    print(L)
    L.sort()
    print(L)
    del L[-1]
    print(L)

if __name__=="__main__":
    main()
