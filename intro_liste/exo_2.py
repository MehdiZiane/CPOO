def main():
    L = [43, -37, 67, 89, 790]
    L.sort()
    borneinf = 0
    bornesup = len(L) - 1
    value = input("enter a number pls: ")
    
    while borneinf <= bornesup:
        mid = (borneinf + bornesup) //2
        if L[mid] < int(value):
            borneinf = mid + 1
        elif L[mid] > int(value):
            bornesup = mid - 1
        else :
            print("congratulation u found the number ")
            return True
    print("your number is not in the list")

if __name__=="__main__":
    main()