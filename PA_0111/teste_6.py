import string
letras = list(string.ascii_lowercase)

letra = input("Digite uma palavra: ")


for i in range(len(letras)):
    if letra == letras[i]:
        print(i)

