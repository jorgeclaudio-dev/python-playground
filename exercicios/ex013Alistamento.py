from datetime import date

ano_atual = date.today().year
ano_nasci = int(input('Ano de Nascimento: '))
idade = ano_atual - ano_nasci
print(f'Quem nasceu em {ano_nasci} tem {idade} anos em {ano_atual}')
if idade < 0 or idade > 100:
    print('Idade Inválida ou não necessária a checagem.')
elif idade == 18:
    print('Você está no ano de se alistar!')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento')
    print(f'Seu alistamento será em {ano_nasci + 18}.')
else:
    print(f'Você já deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {ano_atual - (idade - 18)}.')
