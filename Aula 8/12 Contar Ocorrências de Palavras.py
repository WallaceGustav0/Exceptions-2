from collections import Counter
with open("texto.txt", "r") as file:
    palavras = file.read().split()
contagem = Counter(palavras)
print(contagem)
