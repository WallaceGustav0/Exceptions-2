import os
caminho = input("Digite o caminho do diretório: ")
arquivos = os.listdir(caminho)
print(arquivos)
