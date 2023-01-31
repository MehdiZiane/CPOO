def main():
    animaux = []
    how_many_animals = int(input("enter how many animals you need: "))
    for i in range(how_many_animals):
        animaux.append(input("enter the animal: "))
    print(animaux)
    top = len(animaux) - 1
    temp = animaux[0]
    animaux[0] = animaux[top]
    animaux[top] = temp
    
    print(animaux)

if __name__=="__main__":
    main()