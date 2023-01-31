def main():
    L = [43, -37, 67, 89, 790]
    L.sort()
    print(L)
    number = input("enter a number: ")
    for i in L:
        if i == int(number):
            print("congratulation the number is in the list")
            break
    print("try again")
 
if __name__=="__main__":
    main()