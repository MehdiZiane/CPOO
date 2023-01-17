

nom = input("entrez votre nom : ")
prenom = input("entrez votre prenom : ")
age = input("entrez votre age : ")


if int(age) < 9:
    print("baby")
elif int(age)>= 9 and int(age)<11:
    print("poussin")
elif int(age)>= 11 and int(age)<13:
    print("benjamin")
elif int(age)>=13 and int(age)<15:
    print("minime")
elif int(age)>=15 and int(age)<17:
    print("cadet")
elif int(age)>=17 and int(age)<19:
    print("junior")
elif int(age)>=19 and int(age)<35:
    print("senior")
else :
    print("veteran")