def main():
    animaux = ['chat', 'chien', 'taupe']
    print(animaux)
    compteur = 0
    
    for i in animaux:
        compteur +=1
    temp = animaux[0]
    animaux[0] = animaux[compteur-1]
    animaux[compteur-1] = temp
    
    print(animaux)

if __name__=="__main__":
    main()