def criptografar(texto):
    return ''.join(chr(ord(char) + 1) for char in texto)

def descriptografar(texto):
    return ''.join(chr(ord(char) - 1) for char in texto)

with open("secreto.txt", "r") as file:
    criptografado = criptografar(file.read())
with open("criptografado.txt", "w") as file:
    file.write(criptografado)

#DESCRIPTOGRAFAR
with open("criptografado.txt", "r") as file:
    original = descriptografar(file.read())
print(original)
