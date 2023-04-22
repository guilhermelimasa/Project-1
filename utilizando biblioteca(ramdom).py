import emoji
import random
n = random.randint(1,10)
contador = 1
escolha=int(input("adivinhe o número: "))
if escolha == n:
    print(emoji.emojize("vc acertou de primeira :smiley:",use_aliases=True))
else:
    while escolha != n:
        escolha = int(input("vc errou,tente novamente: "))
        contador += 1
    print(emoji.emojize(f"vc acertou em {contador} tentativas, parabéns :smiley:",use_aliases=True))