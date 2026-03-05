largura = float(input('Qual a largura em metros: '))
altura = float(input('Qual a altura em metros: '))
area = largura * altura
cobertura = 2
tinta = area / cobertura
print(f'Área da parede: {area:.2f} m²')
print(f'Quantidade de tinta necessária: {tinta:.2f} litros')