numero = int(input("digite um número: "))
contador = 1
contador2 = 1
for x in range(numero, 0, -1):
   contador = x * contador
   print(f"{x}x", end=(''))
print(f'= {contador}')
