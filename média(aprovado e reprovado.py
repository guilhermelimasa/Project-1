nome = input("digite o nome do aluno: ")
n1 = float(input("digite sua primeira nota: "))
n2 = float(input("digite sua segunda nota: "))
n3 = float(input("digite sua terceira nota: "))
media = (n1 + n2 + n3) / 3
if media >= 7:
    print("o alune", nome, "foi aprovado :) , sua média foi:", media)
else:
    print("o aluno", nome, "foi reprovado :( , sua média foi:", media)

