num = soma = valor = 0
while True:
    num = int(input('Digite um número: (999 para parar) '))
    if num == 999:
        break
    soma = soma + num
    valor = valor + 1
print(f'A soma dos {valor} valores é {soma}')
