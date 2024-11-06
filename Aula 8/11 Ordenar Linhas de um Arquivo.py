with open("nomes.txt", "r") as file:
    nomes = sorted(file.readlines())
with open("nomes_ordenados.txt", "w") as file:
    file.writelines(nomes)
