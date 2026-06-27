#cria uma lista de caracteres a partir das palavras dadas

jogos = ['MK11', 'Call of duth', 'GTA', "Braw Stars"]

uniao = [c for c in "".join(jogos) if c != " "]

print(uniao)