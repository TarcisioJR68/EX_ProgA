#usando iteração

'''def achatar(lista):
    l2 = []
    for n in lista:
        if not isinstance(n, list):
            l2.append(n)

        else:
            l2.extend(achatar(n))

    return l2'''

#usando compreensão

def achatar(lista):
    return [
        
    ]
    

lista = [1, 2, [4, 2], 5, [2, [1, 2, 3], [[1]]], 8]
print(achatar(lista))

