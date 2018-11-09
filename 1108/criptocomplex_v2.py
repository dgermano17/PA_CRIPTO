import string
letras = list(string.ascii_lowercase)

palavra = input("Digite uma palavra: ")
chave = eval(input("Digite uma chave: "))
crip = list(palavra)
palavra_crip = palavra
inP = 0
inL = 0

for inP in range (len(palavra)):
    while palavra[inP] != letras[inL]:
        inL = inL + 1

    inL = inL + chave

    while inL >= len(letras):
        inL = inL - 26

    while inL < 0:
        inL = inL + 26

    crip[inP] = letras[inL]
    inL = 0

palavra_crip=''.join(crip)
print(palavra_crip)
