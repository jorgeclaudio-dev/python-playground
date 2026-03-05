idade = int(input('Quantos anos você tem: '))
if idade < 0 or idade > 110:
    print('Idade Inválida')
elif idade < 18:
    print('Menor de idade!')
elif idade <= 65:
    print('Adulto')
else:
    print('Idoso')