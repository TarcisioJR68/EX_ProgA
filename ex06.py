#conta a quantidade de vogais na palavra

nome = input().lower()
numVogais = [1 for c in nome if c in "aeiou"]
print(sum(numVogais))