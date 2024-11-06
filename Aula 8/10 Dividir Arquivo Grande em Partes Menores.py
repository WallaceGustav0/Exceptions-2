with open("grande.txt", "r") as file:
    for i, linha in enumerate(file):
        if i % 100 == 0:
            parte = open(f"parte{i // 100 + 1}.txt", "w")
        parte.write(linha)
        if (i + 1) % 100 == 0:
            parte.close()
