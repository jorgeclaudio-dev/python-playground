n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
x = 0
print(f'O que você gostaria: ')
print('*' * 27)
print('Digite 1 para soma')
print('Digite 2 para subtração')
print('Digite 3 para multiplicação')
print('Digite 4 para divisão')
print('*' * 27)
escolha = int(input('Escolha: '))

if escolha == 1:
    x = n1 + n2
    print(f'A soma entre {n1} + {n2} = {x}')
elif escolha == 2:
    x = n1 - n2
    print(f'A diferença entre {n1} - {n2} = {x}')
elif escolha == 3:
    x = n1 * n2
    print(f'O produto de {n1} x {n2} = {x}')
elif escolha == 4:
    x = n1 / n2
    print(f'A divisão entre {n1} / {n2} = {x}')
else:
    print('Escolha não reconhecível, tente novamente entre 1, 2, 3 e 4')