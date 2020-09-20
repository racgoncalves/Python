
# Funções Gerais

import random
from processamentoImagens import Imagem

def criaMatriz(linhas,colunas):
    matriz = []

    i = 0
    while i < linhas:
        matriz.append([' '] * colunas)
        i += 1

    return matriz

def preencheMatriz10(matriz):
    i = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[0]):
            matriz[i][j] = random.randrange(1,11)
            j += 1
        i += 1

def imprimeMatriz(matriz):
    for linha in matriz:
        print(linha)

def somaMatriz(matriz):
    soma = 0
    for linha in matriz:
        for item in linha:
            soma += item
    return soma

def inverteMatriz(matriz):
    matrizInvertida = criaMatriz(len(matriz), len(matriz[0]))
    l = 0
    j = len(matriz[0]) - 1

    while j >= 0:
        i = 0
        k = 0
        while i < len(matriz):
            matrizInvertida[k][l] = matriz[i][j]
            i += 1
            k += 1
        j -= 1
        l += 1

def rotacionaMatriz180(matriz):
    matrizRotacionada = criaMatriz(len(matriz), len(matriz[0]))
    l = 0
    j = len(matriz[0]) - 1

    while j >= 0:
        i = len(matriz)-1
        k = 0
        while i >= 0:
            matrizRotacionada[k][l] = matriz[i][j]
            i -= 1
            k += 1
        j -= 1
        l += 1

    return matrizRotacionada

def rotacionaMatriz90(matriz):
    matrizRotacionada = criaMatriz(len(matriz[0]),len(matriz))
    k = 0
    j = 0

    while j < len(matriz[0]):
        i = len(matriz)-1
        l = 0
        while i >= 0:
            matrizRotacionada[k][l] = matriz[i][j]
            l += 1
            i -= 1
        j += 1
        k += 1

    return matrizRotacionada

def rotacionaMatriz270(matriz):
    matrizRotacionada = criaMatriz(len(matriz[0]),len(matriz))
    k = 0
    j = len(matriz[0]) - 1

    while j >= 0:
        i = 0
        l = 0
        while i < len(matriz):
            matrizRotacionada[k][l] = matriz[i][j]
            l += 1
            i += 1
        j -= 1
        k += 1

    return matrizRotacionada

def recortaImagemColorida(matrizColorida,posLin,posCol,largura,altura):
    red = matrizColorida[0]
    green = matrizColorida[1]
    blue = matrizColorida[2]
    redRecortado = []
    greenRecortado = []
    blueRecortado = []
    linha = posLin

    while len(red) < altura:
        linhaR = []
        linhaG = []
        linhaB = []
        coluna = posCol
        while len(linhaR) < largura:
            linhaR.append(red[linha][coluna])
            linhaG.append(green[linha][coluna])
            linhaB.append(blue[linha][coluna])
            coluna += 1
        redRecortado.append(linhaR)
        greenRecortado.append(linhaG)
        blueRecortado.append(linhaB)
        linha += 1
    return redRecortado,greenRecortado,blueRecortado

def recortaImagemCinza(matriz,posLin,posCol,largura,altura):
    linha = posLin
    matrizRecortada = []

    while len(matrizRecortada) < altura:
        linhaM = []
        coluna = posCol
        while len(linha) < largura:
            linhaM.append(matriz[linha][coluna])
            coluna += 1
        matrizRecortada.append(linhaM)
        linha += 1

    return matrizRecortada

# Exercício 01
'''
tabuleiro = criaMatriz(3,3)

tabuleiro[0][0] = 'x'
tabuleiro[0][1] = 'o'
tabuleiro[0][2] = 'x'
tabuleiro[1][0] = 'O'
tabuleiro[1][1] = 'x'
tabuleiro[2][0] = 'O'
tabuleiro[2][2] = 'X'

imprimeMatriz(tabuleiro)
'''

# Exercício 02
'''
def getDimensao(mat):
    linhas = len(mat)
    colunas = len(mat[0])
    return linhas,colunas

def preencheMatriz(matriz):
    i = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[0]):
            matriz[i][j] = random.random()
            j += 1
        i += 1

matriz = criaMatriz(4,5)

preencheMatriz(matriz)

imprimeMatriz(matriz)

print("\nLinhas",getDimensao(matriz)[0],"x",getDimensao(matriz)[1],"Colunas")
'''

# Exercício 03
'''
def preencheMatriz(matriz):
    i = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[0]):
            matriz[i][j] = random.randrange(0,1001)
            j += 1
        i += 1

matriz = criaMatriz(5,7)
preencheMatriz(matriz)
imprimeMatriz(matriz)
'''

# Exercício 04
'''
def preencheMatriz(matriz):
    i = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[0]):
            matriz[i][j] = random.randrange(-100,101)
            j += 1
        i += 1

# def somaPos(matriz):
#     soma = 0
#     i = 0
#     while i < len(matriz):
#         j = 0
#         while j < len(matriz[0]):
#             if matriz[i][j] > 0: soma += matriz[i][j]
#             j += 1
#         i += 1
#     return soma
 
# usando FOR   
def somaPos(matriz):
    soma = 0
    for linha in matriz:
        for item in linha:
            if item > 0: soma += item
    return soma

matriz = criaMatriz(3,4)
preencheMatriz(matriz)
imprimeMatriz(matriz)
print("\nA soma de todos elementos positivos da matriz é",somaPos(matriz))
'''

# Exercício 05
'''
def preencheMatriz(matriz):
    i = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[0]):
            matriz[i][j] = random.randrange(-100,101)
            j += 1
        i += 1

# usando WHILE
# def soma(matriz):
#     somaPos = 0
#     somaNeg = 0
#     i = 0
#     while i < len(matriz):
#         j = 0
#         while j < len(matriz[0]):
#             if matriz[i][j] > 0: somaPos += matriz[i][j]
#             if matriz[i][j] < 0: somaNeg += matriz[i][j]
#             j += 1
#         i += 1
#     return somaPos,somaNeg

# usando FOR
def soma(matriz):
    somaPos = 0
    somaNeg = 0

    for linha in matriz:
        for item in linha:
            if item > 0: somaPos += item
            if item < 0: somaNeg += item
    return somaPos, somaNeg

matriz = criaMatriz(3,4)
preencheMatriz(matriz)
imprimeMatriz(matriz)
print("\nA soma dos elementos positivos da matriz é",soma(matriz)[0],
      "\nA soma dos elementos negativos da matriz é",soma(matriz)[1])
'''

# Exercício 06
'''
def preencheMatriz(matriz):
    i = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[0]):
            matriz[i][j] = random.randrange(0,10)
            j += 1
        i += 1

def busca(matriz,x):
    linha = -1
    coluna = -1

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == x:
                linha = i
                coluna = j
                break

    return linha, coluna

matriz = criaMatriz(3,3)
preencheMatriz(matriz)
imprimeMatriz(matriz)
x = 4
print("\nA posição de",x,"é",busca(matriz,x)[0],"X",busca(matriz,x)[1])
'''

# Exercício 07
'''
def preencheMatriz(matriz):
    i = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[0]):
            matriz[i][j] = random.randrange(0,256)
            j += 1
        i += 1

def modifica(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] <= 127: matriz[i][j] = 0
            else: matriz[i][j] = 255

matriz = criaMatriz(7,7)
preencheMatriz(matriz)
print("\nMatriz Normal\n")
imprimeMatriz(matriz)
modifica(matriz)
print("\nMatriz Modificada\n")
imprimeMatriz(matriz)
'''

# Exercício 08
'''
def preencheMatriz(matriz):
    i = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[0]):
            matriz[i][j] = random.randrange(1,201)
            j += 1
        i += 1

matriz = criaMatriz(30,50)
conta = [0] * 200
preencheMatriz(matriz)
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        conta[matriz[i][j] -1] += 1

for linha in conta:
    print(linha)
'''

# Exercício 09
'''
def somaLinha(matriz):
    for i in range(len(matriz)):
        soma = 0
        for j in range(len(matriz[0])):
            if j < len(matriz[0])-1: soma += matriz[i][j]
            else: matriz[i][j] = round(soma,2)

matriz = [[100.23,200.94,240.21,110.38,500.29,300.00,""],
          [210.53,302.32,280.51,500.22,750.45,33.01,""],
          [420.67,720.94,430.09,1410.87,567.92,373.43,""],
          [340.89,320.78,480.11,315.80,135.20,900.23,""],
          [650.47,880.49,540.12,99.30,352.26,655.30,""]]

somaLinha(matriz)
for linha in matriz: print(linha)
'''

# Exercício 10 e 11
'''
def somaColuna(matriz):
    for j in range(len(matriz[0])):
        soma = 0
        for i in range(len(matriz)):
            if i < len(matriz)-1: soma += matriz[i][j]
            else: matriz[i][j] = round(soma,2)

def indiceMaior(matriz):
    maiorValor = 0
    indice = 0
    for i in range(len(matriz[0])):
        if matriz[len(matriz)-1][i] > maiorValor:
            maiorValor = matriz[len(matriz)-1][i]
            indice = i

    return indice

matriz = [[100.23,200.94,240.21,110.38,500.29,300.00],
          [210.53,302.32,280.51,500.22,750.45,33.01],
          [420.67,720.94,430.09,1410.87,567.92,373.43],
          [340.89,320.78,480.11,315.80,135.20,900.23],
          ["","","","","",""]]

somaColuna(matriz)
for linha in matriz: print(linha)
print("\nO índice da coluna com o maior valor é",indiceMaior(matriz))
'''

# Exercício 12
'''
matriz = Imagem.getMatrizImagemColorida("processamentoImagens/lago_canada.jpg")

red = matriz[0]
green = matriz[1]
blue = matriz[2]

gray = criaMatriz(len(red),len(red[0]))

for i in range(len(gray)):
    for j in range(len(gray[0])):
        gray[i][j] = ((0.30 * red[i][j]) + (0.59 * green[i][j]) + (0.11 * blue[i][j]))

Imagem.salvaImagemCinza("processamentoImagens/lago_canadaCinza.jpg", gray)
'''

# Exercício 13
'''
# Inverte imagem cinza
matriz = Imagem.getMatrizImagemCinza("processamentoImagens/olhos.jpg")

matrizInvertida = inverteMatriz(matriz)

Imagem.salvaImagemCinza("processamentoImagens/olhosInvertidos.jpg", matrizInvertida)

# Inverte imagem colorida
matriz = Imagem.getMatrizImagemColorida("processamentoImagens/naturezaMorta.jpg")

red = matriz[0]
green = matriz[1]
blue = matriz[2]

redInvertido = inverteMatriz(red)
greenInvertido = inverteMatriz(green)
blueInvertido = inverteMatriz(blue)

Imagem.salvaImagemColorida("processamentoImagens/naturezaMortaInvertida.jpg",redInvertido,greenInvertido,blueInvertido)

# Ponta-cabeça imagem cinza
matriz = Imagem.getMatrizImagemCinza("processamentoImagens/olhos.jpg")

matriz.reverse()

Imagem.salvaImagemCinza("processamentoImagens/olhosPontacabeca.jpg", matriz)

# Ponta-cabeça imagem colorida
matriz = Imagem.getMatrizImagemColorida("processamentoImagens/naturezaMorta.jpg")

matriz[0].reverse()
matriz[1].reverse()
matriz[2].reverse()

Imagem.salvaImagemColorida("processamentoImagens/naturezaMortaPontacabeca.jpg",matriz[0],matriz[1],matriz[2])
'''

# Exercício 14
'''
# Rotaciona imagem cinza 180º
matriz = Imagem.getMatrizImagemCinza("processamentoImagens/olhos.jpg")

matrizRotacionada180 = rotacionaMatriz180(matriz)

Imagem.salvaImagemCinza("processamentoImagens/olhosRotacionados180.jpg", matrizRotacionada180)

# Rotaciona imagem colorida 180º
matriz = Imagem.getMatrizImagemColorida("processamentoImagens/naturezaMorta.jpg")

red = matriz[0]
green = matriz[1]
blue = matriz[2]

redRotacionado180 = rotacionaMatriz180(red)
greenRotacionado180 = rotacionaMatriz180(green)
blueRotacionado180 = rotacionaMatriz180(blue)

Imagem.salvaImagemColorida("processamentoImagens/naturezaMortaRotacionada180.jpg",redRotacionado180,greenRotacionado180,blueRotacionado180)

# Rotaciona imagem cinza 90º
matriz = Imagem.getMatrizImagemCinza("processamentoImagens/olhos.jpg")

matrizRotacionada90 = rotacionaMatriz90(matriz)

Imagem.salvaImagemCinza("processamentoImagens/olhosRotacionados90.jpg", matrizRotacionada90)

# Rotaciona imagem colorida 90º
matriz = Imagem.getMatrizImagemColorida("processamentoImagens/naturezaMorta.jpg")

red = matriz[0]
green = matriz[1]
blue = matriz[2]

redRotacionado90 = rotacionaMatriz90(red)
greenRotacionado90 = rotacionaMatriz90(green)
blueRotacionado90 = rotacionaMatriz90(blue)

Imagem.salvaImagemColorida("processamentoImagens/naturezaMortaRotacionada90.jpg",redRotacionado90,greenRotacionado90,blueRotacionado90)

# Rotaciona imagem cinza 270º
matriz = Imagem.getMatrizImagemCinza("processamentoImagens/olhos.jpg")

matrizRotacionada270 = rotacionaMatriz270(matriz)

Imagem.salvaImagemCinza("processamentoImagens/olhosRotacionados270.jpg", matrizRotacionada270)

# Rotaciona imagem colorida 270º
matriz = Imagem.getMatrizImagemColorida("processamentoImagens/naturezaMorta.jpg")

red = matriz[0]
green = matriz[1]
blue = matriz[2]

redRotacionado270 = rotacionaMatriz270(red)
greenRotacionado270 = rotacionaMatriz270(green)
blueRotacionado270 = rotacionaMatriz270(blue)

Imagem.salvaImagemColorida("processamentoImagens/naturezaMortaRotacionada270.jpg",redRotacionado270,greenRotacionado270,blueRotacionado270)
'''

# Exercício 15
'''
def checaSudoku(matriz):
    colunas = criaMatriz(9, 9)

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            colunas[i][j] = matriz[j][i]

    boolean = True

    for i in range(len(matriz)):
        checagem = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(len(matriz[0])):
            if matriz[i][j] in checagem:
                checagem.pop(checagem.index(matriz[i][j]))
        if len(checagem) != 0: boolean = False

    for i in range(len(colunas)):
        checagem = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(len(colunas[0])):
            if colunas[i][j] in checagem:
                checagem.pop(checagem.index(colunas[i][j]))
        if len(checagem) != 0: boolean = False

    return boolean

# Sorteia números da matriz

# def criaMatrizSudoku():
#     matriz = []
#     i = 0
#     while i < 9:
#         linha = random.sample(range(1, 10), 9)
#         matriz.append(linha)
#         i += 1
#     return matriz
#
# matriz = criaMatrizSudoku()
# imprimeMatriz(matriz)

# Matriz Falsa

# matriz = [[5, 1, 8, 4, 9, 7, 2, 6, 3],
#           [6, 1, 7, 8, 4, 3, 5, 2, 9],
#           [3, 1, 6, 2, 5, 9, 7, 8, 4],
#           [6, 3, 9, 5, 2, 4, 1, 8, 7],
#           [1, 8, 4, 5, 3, 6, 9, 7, 2],
#           [8, 3, 9, 1, 4, 6, 5, 2, 7],
#           [4, 3, 6, 7, 8, 9, 1, 2, 5],
#           [6, 1, 7, 2, 5, 8, 9, 4, 3],
#           [7, 1, 6, 4, 3, 8, 5, 9, 2]]

# Matriz Verdadeira

matriz = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
          [6, 7, 2, 1, 9, 5, 3, 4, 8],
          [1, 9, 8, 3, 4, 2, 5, 6, 7],
          [8, 5, 9, 7, 6, 1, 4, 2, 3],
          [4, 2, 6, 8, 5, 3, 7, 9, 1],
          [7, 1, 3, 9, 2, 4, 8, 5, 6],
          [9, 6, 1, 5, 3, 7, 2, 8, 4],
          [2, 8, 7, 4, 1, 9, 6, 3, 5],
          [3, 4, 5, 2, 8, 6, 1, 7, 9]]

resultado = checaSudoku(matriz)

if (resultado): print("\nÉ uma solução válida de Sudoku")
else: print("\nNão é uma solução válida de Sudoku")
'''

# Exercício 16
'''
# Negativo de imagem cinza
matriz = Imagem.getMatrizImagemCinza("processamentoImagens/olhos.jpg")

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = 255 - matriz[i][j]

Imagem.salvaImagemCinza("processamentoImagens/olhosNegativo.jpg", matriz)

# Negativo de imagem Colorida
matrizColorida = Imagem.getMatrizImagemColorida("processamentoImagens/lago_canada.jpg")

red = matrizColorida[0]
green = matrizColorida[1]
blue = matrizColorida[2]

for i in range(len(red)):
    for j in range(len(red[0])):
        red[i][j] = 255 - red[i][j]

for i in range(len(green)):
    for j in range(len(green[0])):
        green[i][j] = 255 - green[i][j]

for i in range(len(blue)):
    for j in range(len(blue[0])):
        blue[i][j] = 255 - blue[i][j]

Imagem.salvaImagemColorida("processamentoImagens/lago_canadaNegativo.jpg",red,green,blue)
'''

# Exercício 17
'''
# Recorta Imagem Colorida

matrizColorida = Imagem.getMatrizImagemColorida("processamentoImagens/gato.jpg")

print("Altura",len(matrizColorida[0]),"X",len(matrizColorida[0][0]),"Largura")

posLin = 50
posCol = 100
altura = 200
largura = 300

matrizRecortada = recortaImagemColorida(matrizColorida,posLin,posCol,largura,altura)

Imagem.salvaImagemColorida("processamentoImagens/gatoRecortado.jpg",matrizRecortada[0],matrizRecortada[1],matrizRecortada[2])

# Recorta Imagem Cinza

matriz = Imagem.getMatrizImagemCinza("processamentoImagens/yao-ming.jpg")

print("Altura",len(matriz),"X",len(matriz[0]),"Largura")

posLin = 300
posCol = 100
altura = 70
largura = 130

matrizRecortada = recortaImagemCinza(matriz, posLin, posCol, largura, altura)

Imagem.salvaImagemCinza("processamentoImagens/yao-mingRecortado.jpg", matrizRecortada)

# Recorta os dominós

matriz = Imagem.getMatrizImagemCinza("processamentoImagens/domino.jpg")

print("Altura",len(matriz),"X",len(matriz[0]),"Largura")

contX = 0
contY = 0
x=0
y=0
posLin = 5
posCol = 10
altura = 43
largura = 68

while contY < 6:
    while contX < 5:
        matrizRecortada = recortaImagemCinza(matriz, posLin, posCol, largura, altura)
        str = "processamentoImagens/Domino/domino{}{}.jpg"
        str = str.format(x, y)
        Imagem.salvaImagemCinza(str, matrizRecortada)
        if y == 6:
            y = x + 1
            x += 1
        else: y += 1
        if x > 6 or y > 6: break
        posCol += 68
        contX += 1
    posCol = 10
    largura = 68
    posLin += 43
    contY += 1
    contX = 0
'''

# Exercício 18
'''
matrizColorida = Imagem.getMatrizImagemColorida("processamentoImagens/lago_canada.jpg")

red = matrizColorida[0]
green = matrizColorida[1]
blue = matrizColorida[2]

for i in range(len(red)):
    for j in range(len(red[0])):
        if j < len(red[0]) / 2:
            if red[i][j] - 50 > 0: red[i][j] -= 50
            else: red[i][j] = 0

for i in range(len(green)):
    for j in range(len(green[0])):
        if j < len(green[0]) / 2:
            if green[i][j] - 50 > 0: green[i][j] -= 50
            else: green[i][j] = 0

for i in range(len(blue)):
    for j in range(len(blue[0])):
        if j < len(blue[0]) / 2:
            if blue[i][j] - 50 > 0: blue[i][j] -= 50
            else: blue[i][j] = 0

Imagem.salvaImagemColorida("processamentoImagens/lago_canadaMeioEscuro.jpg",red,green,blue)
'''

# Exercício 19
'''
def preencheMatriz(matriz):
    i = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[0]):
            matriz[i][j] = random.randrange(1,201)
            j += 1
        i += 1

def preencheHistograma(matriz,conta):
    i = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[0]):
            if i < conta[j]:
                matriz[i][j] = conta[j]
            else: matriz[i][j] = 0
            j += 1
        i += 1

matriz = criaMatriz(30,50)
conta = [0] * 200
preencheMatriz(matriz)
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        conta[matriz[i][j] -1] += 1

histograma = criaMatriz(max(conta),len(conta))

preencheHistograma(histograma,conta)
histograma = rotacionaMatriz180(histograma)

for i in range(len(histograma)):
    for j in range(len(histograma[0])):
        if histograma[i][j] > 0: histograma[i][j] = 0
        else: histograma[i][j] = 255

Imagem.salvaImagemCinza("processamentoImagens/histograma.jpg", histograma)
'''

