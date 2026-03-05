soma = 0

while True:
    valor = input('Digite um número (Ou "fim" para terminar): ')

    if valor.lower() == 'fim':
        break

    try:
        numero = float(valor)
        soma += numero
    except ValueError:
        print('Digite apenas números válidos.')

print(f'\nA soma total é: R$ {soma:.2f}')