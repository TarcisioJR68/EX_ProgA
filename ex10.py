#exibe positivos

numeros = list(map(int, input().split()))
positivos = [n for n in numeros if n >= 0]
print(positivos)