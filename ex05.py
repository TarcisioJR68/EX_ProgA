#filtra por palavras maiores que 5 letras

nomes = [nome for nome in input().split() if len(nome) > 5]
print(nomes)