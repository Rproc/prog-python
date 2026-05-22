# Construa um programa que só aceite 
# notas escolares entre zero e dez

nota = float(input('Digite uma nota: '))

while nota < 0 or nota > 10:
    print('Nota fora do padrão (0 à 10)')
    nota = float(input('Digite uma nota: '))
