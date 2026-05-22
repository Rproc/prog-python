import math

potencia_lampada = 5.5
largura = 3.5
comprimento = 5.25

# area -> descobrir metragem
area = largura * comprimento
# descobrir quantos watts eu preciso
potencia_necessaria = area * 3
# descobrir numero de bocais
num_bocais = math.ceil(area/3)
# calcular a qtd de lampadas
qtd_lampadas = math.ceil(
potencia_necessaria/potencia_lampada)

print(f'Potencia Necessaria: {potencia_necessaria}')
print(f'Qtd. Lampadas: {qtd_lampadas}')
print(f'Numero Bocais: {num_bocais}')
if qtd_lampadas > num_bocais:
    print('Precisamos de lampadas mais fortes')
else:
    print('Tudo iluminado')