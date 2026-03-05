from datetime import date

ano_atual = date.today().year
ano_nasci = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nasci
print(f'Atleta tem {idade} anos.')

if idade < 2 or idade > 105:
    print(f'Idade Incompatível com a classificação')
elif idade < 10:
    print('Classificação MIRIM')
elif idade < 15:
    print('Classificação INFANTIL')
elif idade < 20:
    print('Classificação JUNIOR')
elif idade <= 25:
    print('Classificação SÊNIOR')
else:
    print('Classificação MASTER')
