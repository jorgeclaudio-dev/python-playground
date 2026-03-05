salario = float(input('Salário Atual: R$ '))
percentual = 0.15
aumento = salario * percentual
novoSalario = salario + aumento
print(f'Salário Antigo: R$ {salario:.2f}')
print(f'Aumento: R$ {aumento:.2f}')
print(f'Novo Salário: R$ {novoSalario:.2f}')