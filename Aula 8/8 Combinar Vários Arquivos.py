with open("texto_completo.txt", "w") as completo:
    for parte in ["parte1.txt", "parte2.txt", "parte3.txt"]:
        with open(parte, "r") as file:
            completo.write(file.read() + "\n")
