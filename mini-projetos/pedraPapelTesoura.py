import random
pc_escolha = ['Pedra', 'Papel', 'Tesoura']
pc = random.choice(pc_escolha)

print('-=-' * 4, 'Pedra, Papel ou Tesoura!', '-=-' * 4)
print(
    '[ 0 ] Para jogar Pedra\n'
    '[ 1 ] Para jogar Papel\n'
    '[ 2 ] Para jogar Tesoura\n'
)
user = int(input('Qual sua jogada: '))

if user not in [0, 1, 2]:
    print('Escolha inválida, escolha entre 0, 1 e 2')

elif user == 0: # Pedra
    print(f'Computador jogou {pc}!')
    print('Você jogou Pedra!')
    if pc == 'Pedra':
        print('EMPATE')
    elif pc == 'Tesoura':
        print('JOGADOR VENCE')
    else:
        print('JOGADOR PERDE')

elif user == 1: # Papel
    print(f'Computador jogou {pc}!')
    print('Jogador jogou Papel!')
    if pc == 'Pedra':
        print('JOGADOR VENCE')
    elif pc == 'Tesoura':
        print('JOGADOR PERDE')
    else:
        print('EMPATE')

else: # Tesoura
    print(f'Computador jogou {pc}!')
    print('Jogador jogou Tesoura!')
    if pc == 'Pedra':
        print('JOGADOR PERDE')
    elif pc == 'Papel':
        print('JOGADOR VENCE')
    else:
        print('EMPATE')

print('-=-' * 4, 'Fim de jogo!', '-=-' * 4)
