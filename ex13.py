#exibe apenas os números pares na matriz

M = [[2,4,6], [2,4,5]]
pares = [n for j in M for n in j if n % 2 == 0]
print(pares)