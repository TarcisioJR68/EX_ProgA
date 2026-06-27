#lista de pares

numeros = list(map(int, input().split()))
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)