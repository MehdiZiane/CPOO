import pprint

def lng_list(List):
    """ 
    input : a list of char
    output : return a dictionnary where the name are the keys and the length of the name is the value
    """
    lng_dct = {}
    for i in List:
        lng = len(i)
        if i not in lng_dct:
            lng_dct[i] = lng
    return lng_dct

def list_value(dct):
    '''
    input : a dictionnary
    output : return a list from all the values in the dictionnary
    '''
    List = []
    for i in dct.values():
        List.append(i)
    return List

def from_list_to_dct(keylist, valuelist):
    '''
    input : 2 list
    output  : return a dictionnary the key are from one list and value from the other
    '''
    dct = {}
    for i in range(min(len(keylist), len(valuelist))):
        dct[keylist[i]] = valuelist[i]
    '''
    for i, k in enumerate(keylist): #enumarate do the same
        if i < len(valuelist):
            dct[k] = valuelist[i]
    '''
    return dct

def sort_list(dct):
    '''
    input : a dictionnary
    output : return a sort list from the key of the dictionnary
    '''
    List = []
    for i in dct.keys():
        List.append(i)
    List.sort()
    return List

def main():
    dct = {'nom' :'Ziane', 'prenom':'Mehdi', 'age' : '22', 'ville':'Charleroi'}
    name_list = ['chat', 'chien', 'rat', 'crocodile']
    second_list = [321, 543, 34, 5]
    pprint.pprint(dct)
    if 'pays' not in dct:
        dct['pays'] = 'Belgique'
    for i in dct.items():
        print(i)
    lng_list(name_list)
    list_value(dct)
    from_list_to_dct(name_list, second_list)
    sort_list(dct)
if __name__ =='__main__':
    main() 