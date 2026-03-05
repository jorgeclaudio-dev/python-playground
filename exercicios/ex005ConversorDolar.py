real = float(input('Quantos reais você tem na carteira: R$ '))
cotacao = 5.0
dolares = real / cotacao
print(f'Você tem R$ {real:.2f}')
print(f'Com isso você pode comprar US$ {dolares:.2f}')