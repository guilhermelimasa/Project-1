n = int(input('digite o numero aqui: !'))
calculando = 1
fatorial = 1
for c in range (n,0,-1):
    calculando = c
    fatorial = calculando*fatorial
    print(f"{c}x", end=(''))

print(f'= {fatorial}')