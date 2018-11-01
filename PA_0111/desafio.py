import string
letras = list(string.ascii_lowercase)

palavra = input("Digite uma palavra: ")


for i in range(len(palavra)):
    for i2 in range(len(letras)):
        if palavra[i] == letras[i2]:
            print(i2)

