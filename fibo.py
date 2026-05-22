# parar no numero 2000 da sequencia

# 0 1 1 2 3 5

anterior = 0
atual = 1
proximo = anterior + atual # 1 = 1 + 0

while proximo < 2000:
    anterior = atual # 1
    atual = proximo # 1
    proximo = anterior + atual # 2 = 1 + 1
    print(proximo)

n = 10
soma = 0
for i in range(1, n):
    x = (n*(n+1))/2
    soma = soma + x