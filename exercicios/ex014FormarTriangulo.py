A = float(input('Primeiro Lado: '))
B = float(input('Segundo Lado: '))
C = float(input('Terceiro Lado: '))

if A < B + C and B < A + C and C < A + B:
    if A == B and B == C:
        print('Triângulo Equilátero')
    elif A == B or A == C or B == C:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')
else:
    print('Não Forma Um Triângulo')