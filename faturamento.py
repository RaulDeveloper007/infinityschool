valor_fixo = float(input("Digite o valor da tonelada: "))
tonelada_total = 0
tonelada = 1

while tonelada > 0:
    tonelada = float(input("Quantas toneladas sairam?"))
    tonelada_total += tonelada

faturamento_total = tonelada_total * valor_fixo
print(f"O valor total faturado foi: {faturamento_total} reais")