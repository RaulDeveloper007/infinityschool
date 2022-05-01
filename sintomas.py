assintomatico = 0
leve = 0
grave = 0
paciente = 0
contador = 1

while contador < 11:
    paciente = int(input("Digite o sintoma (1 - assintomático, 2 - leve, 3 - grave): "))
    if paciente == 1:
        print('assintomático')
        assintomatico += 1
        contador += 1
    elif paciente == 2:
        print('leve')
        leve += 1
        contador += 1
    elif paciente == 3:
        print('grave')
        grave += 1
        contador += 1
    else:
        print(
            'Digito inválido. Digite "1" para paciente assintomático, "2" para sintomas leves e "3" para sintomas graves: ')

print(
    f"O percentual dos sintomas foi: {assintomatico * 100 / 10}%, para assintomáticos, {leve * 100 / 10}%, para sintomas leves e {grave * 100 / 10}%, para sintomas graves.")