with open("pessoas.txt", "r") as file:
    for linha in file:
        if "Nome:" in linha:
            nome = linha.split(",")[0].replace("Nome: ", "").strip()
            print(nome)
