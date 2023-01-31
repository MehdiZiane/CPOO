def main():
    word = input("enter a word pls: ")
    compteur = 0
    
    for i in (word):
        compteur += 1
        if i == " " or i =="_" or i =="-":
            compteur -= 1
    print(compteur)
if __name__=="__main__":
    main()