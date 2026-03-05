idade = int(input('Qual sua idade: '))
while idade < 0 or idade > 110:
    print(f'A idade {idade} é inválida! Tente Novamente.')
    idade = int(input('Qual sua idade: '))
print('FIM')