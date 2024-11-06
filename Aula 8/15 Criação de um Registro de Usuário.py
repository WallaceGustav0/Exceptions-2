nome = input("Nome: ")
idade = input("Idade: ")
email = input("Email: ")
with open("usuarios.txt", "a") as file:
    file.write(f"{nome}, {idade}, {email}\n")
