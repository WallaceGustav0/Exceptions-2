with open("origem.txt", "r") as origem, open("copia.txt", "w") as copia:
    conteudo = origem.read()
    copia.write(conteudo)
