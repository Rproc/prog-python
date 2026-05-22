# altura, largura, comprimento
# caixa = 1.5 metros
import math

altura = 4
largura = 4.5
comprimento = 7.5
caixa = 1.5

area_parede = (
    2*(altura*largura) +
    2*(altura*comprimento)
)
qtd_caixas = math.ceil(area_parede/caixa)

print(f'Numero de caixas: {qtd_caixas}')




nota = 10
nota1 = 5
nota2 = 8

nota = nota + nota1





