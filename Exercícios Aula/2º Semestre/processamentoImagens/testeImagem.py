import Imagem

matriz = Imagem.getMatrizImagemCinza("olhos.jpg")

print("Altura: ", len(matriz))
print("Largura: ", len(matriz[0]))

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] += 100

Imagem.salvaImagemCinza("olhosClaro.jpg", matriz)