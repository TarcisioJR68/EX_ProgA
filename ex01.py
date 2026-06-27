#retorna uma lista com os números digitados em uma linha

def leiaTeclado():
    return [n for n in map(int, input().split())]

print(leiaTeclado())