frase = input("Digite uma frase: ")
with open("anotacoes.txt", "a") as file:
    file.write(frase + "\n")
