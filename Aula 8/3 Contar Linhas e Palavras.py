with open("texto.txt", "r") as file:
    linhas = file.readlines()
    num_linhas = len(linhas)
    num_palavras = sum(len(linha.split()) for linha in linhas)
    print(f"Linhas: {num_linhas}, Palavras: {num_palavras}")
