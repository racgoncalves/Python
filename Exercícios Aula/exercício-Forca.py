
from unicodedata import normalize

def removerAcentos(txt):
  return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

def montaPalavraOculta (acertos,palavra):
    palavraOculta = ""
    for i in range(0,len(palavra)):
        if removerAcentos(palavra[i].lower()) in acertos:
            palavraOculta += palavra[i]
        else:
            palavraOculta += "_"
    return palavraOculta

def checaLetra(letra,palavra):
    acertos = " "
    erros = ""
    vida = 0
    if letra in removerAcentos(palavra.lower()):
        acertos += letra
    else:
        erros += letra + " "
        vida = 1
    return acertos,erros,vida

vida = 0
letra = ""
acertos = ""
erros = ""
palavraOculta = ""

palavra = input("Digite uma palavra: ")

while vida <= 0:
    try:
        vida = int(input("Digite a quantidade de vidas (mínimo 1): "))
    except:
        print("\nDigite apenas números!")
        vida = 0

while vida > 0 and palavra != palavraOculta:

    while (len(letra) != 1 or letra in erros or letra in acertos or not letra.isalpha()):
        letra = removerAcentos(input("Digite uma letra: ").lower())
        if letra in erros or letra in acertos:
            print("\nVocê já digitou essa letra")
        elif len(letra) != 1:
            print("\nVocê só pode digitar uma única letra")
        elif not letra.isalpha():
            print("\nVocê deve digitar apenas letra")

    resultado = checaLetra(letra,palavra)
    letra = ""
    acertos += resultado[0]
    erros += resultado[1]
    vida -= resultado[2]
    palavraOculta = montaPalavraOculta(acertos,palavra)
    print("\nPalavra oculta:",palavraOculta,"\nLetras erradas:",erros,"\nQuantidade de Vidas:",vida)
    if palavra == palavraOculta:
        print("\nParabéns, você ganhou!")
    elif vida == 0:
        print("\nVocê foi enforcado!")