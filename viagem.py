tempoViagem = float(input('Informe o tempo gasto na viagem: '))
velocidadeMedia = float(input('Informe a velocidade média utilizada na viagem: '))
distancia = tempoViagem * velocidadeMedia
litrosUsados = distancia / 12

print(f'A velocidade média utilizada na viagem foi {velocidadeMedia} km/ h. O tempo gasto na viagem foi {tempoViagem} minutos/ horas. A distância percorrida foi {distancia} km. A quantidade de combustível usada foi {litrosUsados} L. ')