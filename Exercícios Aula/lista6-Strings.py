
def tudoMaiusculo(palavra):
    novaPalavra = palavra.upper()
    return novaPalavra

def separaPalavra(palavra):
    palavraNova = ""
    for i in range(0,len(palavra)):
        palavraNova += palavra[i]
        palavraNova += " "
    return palavraNova

def substituiLetra(frase,letra):
    fraseNova = ""
    for i in range(0,len(frase)):
        maiuscula = letra.upper()
        minuscula = letra.lower()
        if frase[i] == maiuscula or frase[i] == minuscula:
            fraseNova += "*"
        else:
            fraseNova += frase[i]
    return fraseNova

def substituiLetras(frase,letras):
    for i in range(0,len(letras)):
        maiuscula = letras[i].upper()
        minuscula = letras[i].lower()
        frase = frase.replace(maiuscula,"*")
        frase = frase.replace(minuscula,"*")
    return frase

def contaPalavra(frase,palavra):
    cont = 0
    x = 0
    while frase.find(palavra,x) != -1:
        cont += 1
        x = frase.find(palavra,x)
        x += 1
    return cont

#1
palavra = input("Escreva uma palavra para transformar em maiúsculo: ")
print(tudoMaiusculo(palavra))

#2
palavra = input("Escreva uma palavra para separar por espaços: ")
print(separaPalavra(palavra))

#3
frase = input("Escreva uma frase: ")
letra = input("Digite a letra que será substituídas por *: ")
print(substituiLetra(frase,letra))

#4
frase = input("Escreva uma frase: ")
letras = input("Digite as letras que serão substituídas por *: ")
print(substituiLetras(frase,letras))

#5
frase = input("Escreva uma frase: ")
palavra = input("Digite a palavra que será contada na frase: ")
print("Número de vezes que a palavra aparece na frase:",contaPalavra(frase,palavra))