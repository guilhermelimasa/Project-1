nome = "Guilherme"
while True:
    login = input("Digite seu nome de usuário: ")
    if login == nome:
        print("Login bem-sucedido!")
        break
    else:
        print("Nome de usuário incorreto. Tente novamente.")
