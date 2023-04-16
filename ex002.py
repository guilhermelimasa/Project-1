n = int(input("digite um número: "))
soma = 0
contador = 1
while contador <= n:
    if contador % 2 == 0:
        soma+= contador
    contador+=1
print(f"a quantidade de números pares é {n} e a soma entre eles é {soma}")

