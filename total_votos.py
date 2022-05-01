total = input("Informe o total de eleitores do município:")
total = int(total)
brancos = input("Informe a quantidade de votos brancos:")
brancos = int(brancos)
nulos = input("Informe a quantidade de votos nulos:")
nulos = int(nulos)
validos = total - (brancos + nulos)

perc_brancos = brancos * 100 / total
perc_nulos = nulos * 100 / total
perc_validos = validos * 100 / total

print("Votos brancos representam: ", perc_brancos, end = '%. ' ' \n')
print("Votos nulos representam: ", perc_nulos, end = '%. ' '\n')
print("Votos válidos representam: ", perc_validos, end = '%.' '\n')