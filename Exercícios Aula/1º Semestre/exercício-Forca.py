import random
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

facil = ["Amarelo","Amiga","Amor","Ave","Avião","Avó","Balão","Bebê","Bolo","Branco","Cama","Caneca","Celular","Clube","Copo","Doce","Elefante",
        "Escola","Estojo","Faca","Foto","Garfo","Geleia","Girafa","Janela","Limonada","Mãe","Meia","Noite","Óculos","ônibus","Ovo","Pai","Pão",
        "Parque","Passarinho","Peixe","Pijama","Rato","Umbigo"]
dificil = ["Acender","Afilhado","Ardiloso","Áspero","Assombração","Asterisco","Basquete","Caminho","Champanhe","Chiclete","Chuveiro","Coelho",
           "Contexto","Convivência","Coração","Desalmado","Eloquente","Esfirra","Esquerdo","Exceção","Fugaz","Gororoba","Heterossexual",
           "Horrorizado","Impacto","Independência","Modernidade","Oftalmologista","Otorrinolaringologista","Paralelepípedo","Pororoca",
           "Prognósticio","Quarentena","Quimera","Refeição","Reportagem","Sino","Taciturno","Tênue","Visceral"]
aleatorio = ["Afobado","Amendoim","Banheiro","Caatinga","Cachorro","Campeonato","Capricórnio","Catapora","Corrupção","Crepúsculo","Empenhado",
           "Esparadrapo","Forca","Galáxia","História","Magenta","Manjericão","Menta","Moeda","Oração","Paçoca","Palavra","Pedreiro","Pneumonia",
           "Pulmão","Rotatória","Serenata","Transeunte","Trilogia","Xícara"]

palavra = ""
vida = 0
letra = ""
acertos = ""
erros = ""
palavraOculta = ""
opcao = 0

print("\nJOGO DA FORCA")

while opcao <= 0 or opcao > 3:
    try:
        opcao = int(input("\n1 - Fácil\n2 - Difícil\n3 - Aleatório\nDigite o número do nível de dificuldade desejado: "))
        if opcao == 1:
            palavra = facil[random.randrange(len(facil))]
        elif opcao == 2:
            palavra = dificil[random.randrange(len(dificil))]
        elif opcao == 3:
            palavra = aleatorio[random.randrange(len(aleatorio))]
        elif opcao <= 0 or opcao > 3:
            print("\nEscolha uma das opções!")
    except:
         print("\nDigite apenas números!")
         opcao = 0

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
        print("\nPalavra correta:",palavra,"\nVocê foi enforcado!")