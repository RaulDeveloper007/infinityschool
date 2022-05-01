qtd_notas = int(input("Digite quantas notas deseja informar: "))
media = 0

for i in range (qtd_notas):
    nota = float(input("Digite sua nota: "))
    media = media + nota

media = media / qtd_notas
print(f"Média final: {media:.3}")