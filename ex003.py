produto = input("digite o nome do produto: ")
vendas = float(input("digite o número de vendas do produto: "))
preço = float(input("digite o preço desse produto: "))
while vendas < 0:
    print("valor de venda inválido digite outro!")
    vendas = float(input("digite um número de vendas válido: "))
while preço < 0:
    print("preço do produto inválido!")
    preço = float(input("digite um valor de preço válido: "))
soma = vendas * preço
print(f"o {produto} de preço {preço} e o valor da compra deu {soma}")
