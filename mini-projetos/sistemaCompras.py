print('='* 10, 'Loja Jorges', '=' * 10)
valor = float(input('Preço das compras: R$ '))
print(
    'Formas de pagamento\n'
    '[ 1 ] à vista dinheiro/cheque\n'
    '[ 2 ] à vista cartão\n'
    '[ 3 ] 2x no cartão\n'
    '[ 4 ] 3x ou mais vezes no cartão'
)
escolha = int(input('Qual sua escolha: '))
descA = valor * 10 / 100 # desconto à vista ou cheque
descB = valor * 5 / 100 # desconto cartão à vista

if escolha not in [1, 2, 3, 4]:
    print('Escolha inexistente')
elif escolha == 1:
    print(f'Compra à vista de R$ {valor:.2f} vai custar R$ {valor - descA:.2f} no final')
elif escolha == 2:
    print(f'Compra à vista no cartão de R$ {valor:.2f} vai custar R$ {valor - descB:.2f} no final')
elif escolha == 3:
    parcela = valor / 2
    print(f'Compra em 2x de R$ {parcela:.2f} no cartão no valor final de R$ {valor:.2f}')
else:
    parcela = int(input('Quantas parcelas: '))
    juros = valor * 20 / 100
    valor_parcela = (valor + juros) / parcela
    print(f'Compra parcelada em {parcela}x no valor de R$ {valor_parcela:.2f}'
          f' no valor final de R$ {valor + juros:.2f}')
