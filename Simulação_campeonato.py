
# Rodrigo André Chiarelli Gonçalves, RM: 85716

import random

# Forma a linha de cada time
def formaLinha(time):

            #time,pontos,jogos,vitorias,empates,derrotas,gols marcados,gols sofridos, saldo de gols, aproveitamento
    linha = [time,0,0,0,0,0,0,0,0,0]

    return linha

# Forma o campeonato inteiro
def formaCampeonato(times):
    aux = []
    tabela = []

    # Copia a lista de times
    for i in range(len(times)): aux.append(times[i])

    # Coloca em ordem alfabética
    aux.sort()

    i = 0
    while i < 10:

        # Copia sempre o primeiro item
        time = aux.pop(0)

        # Transforma o time numa linha e junta no campeonato
        tabela.append(formaLinha(time))
        i += 1

    return tabela

# Monta a sequência de jogos
def montaAdversarios():

    lista = []

    for i in range(9):
        for j in range(i + 1, 10):
            partida = (i,j)
            lista.append(partida)

    return lista

# Realiza as partidas
def partida(campeonato,timeA,timeB):
    golsA = random.randint(0, 8)
    golsB = random.randint(0, 8)
    pontoA = 0
    vitA = 0
    empA = 0
    derA = 0
    pontoB = 0
    vitB = 0
    empB= 0
    derB = 0

    # Ganha o time A
    if golsA > golsB:
        pontoA = 3
        vitA = 1
        derB = 1

    # Empata
    elif golsA == golsB:
        pontoA = 1
        pontoB = 1
        empA = 1
        empB = 1

    # Ganha o time B
    else:
        pontoB = 3
        vitB = 1
        derA = 1

    # Atualiza os dados do time A
    campeonato[timeA] = [campeonato[timeA][0],                  # time
                            campeonato[timeA][1]+pontoA,        # pontos
                            campeonato[timeA][2]+1,             # jogos
                            campeonato[timeA][3]+vitA,          # vitorias
                            campeonato[timeA][4]+empA,          # empates
                            campeonato[timeA][5]+derA,          # derrotas
                            campeonato[timeA][6]+golsA,         # gols marcados
                            campeonato[timeA][7]+golsB,         # gols sofridos
                            campeonato[timeA][8]+golsA-golsB,   # saldo de gols
                            campeonato[timeA][9]]               # aproveitamentoA

    # Atualiza o aproveitamento do time A
    campeonato[timeA][9] = round(((campeonato[timeA][1] / (campeonato[timeA][2] * 3)) * 100), 1)

    # Atualiza os dados do time B
    campeonato[timeB] = [campeonato[timeB][0],                  # time
                         campeonato[timeB][1] + pontoB,         # pontos
                         campeonato[timeB][2] + 1,              # jogos
                         campeonato[timeB][3] + vitB,           # vitorias
                         campeonato[timeB][4] + empB,           # empates
                         campeonato[timeB][5] + derB,           # derrotas
                         campeonato[timeB][6] + golsB,          # gols marcados
                         campeonato[timeB][7] + golsA,          # gols sofridos
                         campeonato[timeB][8] + golsB - golsA,  # saldo de gols
                         campeonato[timeB][9]]                  # aproveitamentoB

    # Atualiza o aproveitamento do time B
    campeonato[timeB][9] = round(((campeonato[timeB][1] / (campeonato[timeB][2] * 3)) * 100), 1)

    # Retorna os jogos caso queira imprimir
    # return campeonato[timeA][0],golsA,golsB,campeonato[timeB][0]

# Realiza os dois turnos do campeonato
def turnos(competidores):

    # Processa o Primeiro Turno
    # print("\nJogos do Campeonato\n\nPrimeiro Turno\n")
    for i in range(len(competidores)):
        partida(campeonato, competidores[i][0], competidores[i][1])
        # jogo = partida(campeonato,competidores[i][0],competidores[i][1])
        # print(jogo[0],jogo[1],"X",jogo[2],jogo[3])

    # Processa o Segundo Turno
    # print("\nSegundo Turno\n")
    for i in range(len(competidores)):
        partida(campeonato,competidores[i][1],competidores[i][0])
        # jogo = partida(campeonato,competidores[i][1],competidores[i][0])
        # print(jogo[0],jogo[1],"X",jogo[2],jogo[3])

# Imprime a Tabela do Campeonato em ordem alfabética
def imprime(campeonato):

    print("\nTabela do Campeonato em ordem alfabética\n")
    print("       Clube        Pts PJ VIT E  DER GP  GC  SG   %")
    for i in range(len(campeonato)):
        print(campeonato[i])

# Retorna o campeão
def campeao(campeonato):
    maiorPonto = 0
    campeoesPonto = []
    maiorVitoria = 0
    campeoesVitoria = []
    maiorGols = 0
    campeoesGols = []
    campeao = ""

    # Campeão por pontos
    for i in range(len(campeonato)):
        if campeonato[i][1] >= maiorPonto: maiorPonto = campeonato[i][1]
    for i in range(len(campeonato)):
        if campeonato[i][1] == maiorPonto:
            campeoesPonto.append(campeonato[i])
            campeao = campeonato[i][0]
    if len(campeoesPonto) == 1: return campeao

    # Campeão por vitórias
    for i in range(len(campeoesPonto)):
        if campeoesPonto[i][3] >= maiorVitoria: maiorVitoria = campeoesPonto[i][3]
    for i in range(len(campeoesPonto)):
        if campeoesPonto[i][3] == maiorVitoria:
            campeoesVitoria.append(campeoesPonto[i])
            campeao = campeoesPonto[i][0]
    if len(campeoesVitoria) == 1: return campeao

    # Campeão por gols marcados
    for i in range(len(campeoesVitoria)):
        if campeoesVitoria[i][6] >= maiorGols: maiorGols = campeoesVitoria[i][6]
    for i in range(len(campeoesVitoria)):
        if campeoesVitoria[i][6] == maiorGols:
            campeoesGols.append(campeoesVitoria[i])
            campeao = campeoesVitoria[i][0]
    if len(campeoesGols) == 1: return campeao

    # Empates
    return campeoesGols

# Retorna o lanterna
def lanterna(campeonato):
    menorPonto = 54
    lanternasPonto = []
    menorVitoria = 18
    lanternasVitoria = []
    menorGols = 126
    lanternasGols = []
    lanterna = ""

    # Lanterna por pontos
    for i in range(len(campeonato)):
        if campeonato[i][1] <= menorPonto: menorPonto = campeonato[i][1]
    for i in range(len(campeonato)):
        if campeonato[i][1] == menorPonto:
            lanternasPonto.append(campeonato[i])
            lanterna = campeonato[i][0]
    if len(lanternasPonto) == 1: return lanterna

    # Lanterna por vitórias
    for i in range(len(lanternasPonto)):
        if lanternasPonto[i][3] <= menorVitoria: menorVitoria = lanternasPonto[i][3]
    for i in range(len(lanternasPonto)):
        if lanternasPonto[i][3] == menorVitoria:
            lanternasVitoria.append(lanternasPonto[i])
            lanterna = lanternasPonto[i][0]
    if len(lanternasVitoria) == 1: return lanterna

    # Lanterna por gols marcados
    for i in range(len(lanternasVitoria)):
        if lanternasVitoria[i][6] <= menorGols: menorGols = lanternasVitoria[i][6]
    for i in range(len(lanternasVitoria)):
        if lanternasVitoria[i][6] == menorGols:
            lanternasGols.append(lanternasVitoria[i])
            lanterna = lanternasVitoria[i][0]
    if len(lanternasGols) == 1: return lanterna

    # Empates
    return lanternasGols

# <<<<<<<<<<<< FIM DAS FUNÇÕES >>>>>>>>>>>>

# Campeonatos
brasileiro = ["Palmeiras      ", "Corinthians    ", "São Paulo      ", "Santos         ", "Flamengo       ",
              "Fluminense     ", "Botafogo       ", "Vasco          ", "Internacional  ", "Grêmio         "]

espanhol = ["Barcelona      ", "Real Madrid    ", "Atl. de Madrid ", "Valencia       ", "Villareal      ",
            "Alavés         ", "Sevilla        ", "Betis          ", "Espanyol       ", "Celta          "]

ingles = ["Manch. United  ", "Manch. City    ", "Arsenal        ", "Chelsea        ", "Liverpool      ",
          "Tottenham      ", "Leicester      ", "Newcastle      ", "Aston Villa    ", "West Ham       "]

# Menu para escolher o campeonato
times = []
opcao = 0

while opcao == 0:

    try:
        opcao = int(input("1 - Campeonato Brasileiro\n2 - Campeonato Espanhol\n3 - Campeonato Inglês\nDigite o campeonato que deseja rodar: "))
    except:
        print("\nDigite apenas números!\n")
        opcao = 0

    if opcao == 1: times = brasileiro
    elif opcao == 2: times = espanhol
    elif opcao == 3: times = ingles
    elif opcao != 0:
        print("\nNúmero Inválido\n")
        opcao = 0

# Forma o campeonato
campeonato = formaCampeonato(times)

# Monta os confrontos
competidores = montaAdversarios()

# Faz os jogos acontecerem em turno e returno
turnos(competidores)

# Imprime a Tabela após todos os jogos
imprime(campeonato)

# Imprime o campeão
print("\nO campeão foi o:",campeao(campeonato))

# Imprime o lanterna
print("\nO lanterna foi o:",lanterna(campeonato))