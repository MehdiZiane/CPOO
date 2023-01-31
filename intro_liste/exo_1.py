def main():
    animaux = ['chat', 'chien', 'taupe']
    print(animaux)
    top = len(animaux) - 1
    temp = animaux[0]
    animaux[0] = animaux[top]
    animaux[top] = temp
    
    print(animaux)

if __name__=="__main__":
    main()