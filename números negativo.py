negativos = 0 # variável que conta quantos números são negativos

for i in range(10): # loop para ler 10 números
    num = float(input("Digite um número: "))
    if num < 0:
        negativos += 1 # se o número lido for negativo, incrementa a variável negativos

print(f"Foram digitados {negativos} números negativos.")
