primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
for c in range (primeiro, 11, razão):
    print('{}'.format(c), end='->')
    