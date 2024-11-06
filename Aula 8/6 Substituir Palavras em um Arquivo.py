with open("texto.txt", "r") as file:
    conteudo = file.read().replace("Python", "programação")
with open("texto_modificado.txt", "w") as novo_file:
    novo_file.write(conteudo)
