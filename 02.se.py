# ler entrada de um usuario
# o que será lido é uma nota
# deverá falar se o aluno 
# vai ser aprovado (>=7) ou não 

nota = float(input('Digite uma nota\n'))

if nota >= 7:
    print('Aprovado')

else:
    print('Reprovado')