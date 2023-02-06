import pprint

def Age(dct):
    pprint.pprint(dct)

def main():
    first_dico = {'nom' : 'Dupont', 'prenom' : 'Davi', 'age' : 30}
    for i, j in first_dico.items():
        if i =="prenom":
            first_dico[i] = 'David'
    print(list(first_dico.items()))
    print("{0[prenom]:} {0[nom]:} a {0[age]:} ans".format(first_dico))
    if 'date' not in first_dico:
        first_dico['date'] = '17/01/1991'
    pprint.pprint(first_dico)
    Age(first_dico)
if __name__ == "__main__":
    main()