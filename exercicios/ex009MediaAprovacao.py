n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print(f'APROVADO, sua média foi {media:.1f}, meus parabéns!')
else:
    print(f'RECUPERAÇÃO, sua média foi {media:.1f}, estude mais!')