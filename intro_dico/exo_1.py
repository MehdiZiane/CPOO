import pprint
from datetime import datetime
def age(dct):
    today = datetime.now()
    birthdate = datetime.strptime(dct['date'],'%d/%m/%Y')
    age = today.year - birthdate.year
    return age

def main():
    first_dct = {'nom' : 'Dupont', 'prenom' : 'Davi', 'age' : 30}
    for i, j in first_dct.items():
        if i =="prenom":
            first_dct[i] = 'David'
    print(list(first_dct.items()))
    print("{0[prenom]:} {0[nom]:} a {0[age]:} ans".format(first_dct))
    if 'date' not in first_dct:
        first_dct['date'] = '17/01/1991'
    pprint.pprint(first_dct)
    print(age(first_dct))
if __name__ == "__main__":
    main()