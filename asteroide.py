asteroides = [ ]
distancia = [ ]
for i in range (5):
    nome = input('Digite o nome do asteróide: ')
    asteroides.append(nome)
    km = float(input('Digite a distância que esta da terra em km: '))
    distancia.append(km)

print(f'Os nomes dos asteróides são: {asteroides[0], asteroides[1], asteroides[2], asteroides[3], asteroides[4]}')
print(f'As distâncias dos asteróides são {distancia[0], distancia[1], distancia[2], distancia[3], distancia[4]} km')
print(f'A média das distâncias dos asteróides para a Terra é: {(distancia[0] + distancia[1] + distancia[2] + distancia[3] + distancia [4]) / 5} km')





