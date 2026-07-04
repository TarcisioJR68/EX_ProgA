#notas maiores que a média

notas = list(map(float, input().split()))
naMedia = [n for n in notas if n > 5]
print(naMedia)