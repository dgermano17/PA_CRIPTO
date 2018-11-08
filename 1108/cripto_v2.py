import string
letras = list(string.ascii_lowercase)

palavra = input("Digite uma palavra: ")
chave = int(input("Digite uma chave: "))


for i in range(len(palavra)):
    for i2 in range(len(letras)):
        if palavra[i] == letras[i2]:
            i2 = i2 + chave

            while i2 >= len(letras):
                i2 = i2 - 26

            while i2 < 0:
                i2 = i2 + 26

            print(letras[i2])
