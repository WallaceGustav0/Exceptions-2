with open("com_vazios.txt", "r") as file:
    linhas = [linha for linha in file if linha.strip()]
with open("sem_vazios.txt", "w") as file:
    file.writelines(linhas)
