with open("imagem.jpg", "rb") as imagem, open("imagem_copia.jpg", "wb") as copia:
    copia.write(imagem.read())
