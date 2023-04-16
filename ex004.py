from random import randint
numero = randint(0, 10)
tentativa = int(input("tente adivinhar qual é o número: "))
contador = 19
while tentativa != numero:
    print("número errado!!")
    tentativa = int(input("tente novamente: "))
    contador = contador + 1
print(f"vc acertou, foram {contador} tentativas.")