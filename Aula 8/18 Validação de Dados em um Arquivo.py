with open("dados.csv", "r") as dados, open("erros.csv", "w") as erros:
    for linha in dados:
        nome, idade, email = linha.strip().split(", ")
        if not idade.isdigit() or "@" not in email:
            erros.write(linha)
