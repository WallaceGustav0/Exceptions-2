frase = input("Digite uma frase: ")
with open("frase_usuario.txt", "w") as file:
    file.write(frase)
