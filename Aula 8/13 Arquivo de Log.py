from datetime import datetime
with open("dados.txt", "r") as dados, open("backup.txt", "a") as backup:
    backup.write(dados.read())
    backup.write(f"\nBackup realizado em: {datetime.now()}\n")
