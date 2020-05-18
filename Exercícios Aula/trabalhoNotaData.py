
def validaAno(ano):
    return (ano > 0)

def validaMes(mes):
    return (mes > 0 and mes <= 12)

def diasFevereiro(ano):
    if (ano % 400 == 0):
        return 29
    elif (ano % 100 != 0 and ano % 4 == 0):
        return 29
    else:
        return 28

def validaDia(dia, mes, ano):
    listaMes = [31, diasFevereiro(ano), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return (dia > 0 and dia <= listaMes[mes - 1])

def somarDias(data, diaSoma):
    dia = data[0]
    mes = data[1]
    ano = data[2]
    while diaSoma != 0:
        if (validaDia(dia+1,mes,ano)):
            dia += 1
            diaSoma -= 1
        elif (validaMes(mes+1)):
            dia = 1
            mes += 1
            diaSoma -= 1
        else:
            ano += 1
            mes = 1
            dia = 1
            diaSoma -= 1
    return dia, mes, ano

def subtrairDias(data , diaSubtrai):
    dia = data[0]
    mes = data[1]
    ano = data[2]

    while diaSubtrai != 0:
        if (validaDia(dia-1,mes,ano)):
            dia -= 1
            diaSubtrai -= 1
        elif (validaMes(mes-1)):
            mes -= 1
            diaSubtrai -= 1
            if (validaDia(31,mes,ano)):
                dia = 31
            elif (validaDia(30,mes,ano)):
                dia = 30
            elif (validaDia(29,mes,ano)):
                dia = 29
            else:
                dia = 28
        else:
            ano -= 1
            mes = 12
            dia = 31
            diaSubtrai -= 1
    return dia, mes, ano

def diferencaDatas(data,data2):
    cont = 0
    if (data[2] > data2[2]):
        dataMaior = data
        dataMenor = data2
    elif (data[2] < data2[2]):
        dataMaior = data2
        dataMenor = data
    elif (data[1] > data2[1]):
        dataMaior = data
        dataMenor = data2
    elif (data[1] < data2[1]):
        dataMaior = data2
        dataMenor = data
    elif (data[0] > data2[0]):
        dataMaior = data
        dataMenor = data2
    elif (data[0] < data2[0]):
        dataMaior = data2
        dataMenor = data
    else:
        return cont
    while (dataMenor[0] != dataMaior[0] or dataMenor[1] != dataMaior[1] or dataMenor[2] != dataMaior[2]):
        cont += 1
        dataMenor = somarDias(dataMenor, 1)
    return cont

def geraData():
    ano = int(input("Digite um ano: "))
    while (validaAno(ano) == False):
        print("\nAno Inválido!\n")
        ano = int(input("Digite um ano: "))
    mes = int(input("Digite um mês: "))
    while (validaMes(mes) == False):
        print("\nMês Inválido!\n")
        mes = int(input("Digite um mês: "))
    dia = int(input("Digite um dia: "))
    while (validaDia(dia,mes,ano) == False):
        print("\nDia Inválido!\n")
        dia = int(input("Digite um dia: "))
    return dia, mes, ano

print("\nCalculadora de Datas")
menu = 0
while (menu!= 4):
    menu = int(input("\n1 - Somar dias em uma data\n2 - Subtrair dias de uma data\n3 - Encontrar a diferença de dias entre duas datas"
                     "\n4 - Encerrar o programa\nDigite o código da operação desejada: "))
    if (menu == 1):
        print("\nGerando a data")
        data = geraData()
        print("Você gerou a seguinte data:",data[0],"/",data[1],"/",data[2])
        diaSoma = int(input("Digite a quantidade de dias que deseja somar: "))
        novaData = somarDias(data,diaSoma)
        print("\nSua nova data é",novaData[0],"/",novaData[1],"/",novaData[2])
    elif (menu == 2):
        print("\nGerando a data")
        data = geraData()
        print("Você gerou a seguinte data:", data[0], "/", data[1], "/", data[2])
        diaSubtrai = int(input("Digite a quantidade de dias que deseja subtrair: "))
        novaData = subtrairDias(data, diaSubtrai)
        print("\nSua nova data é",novaData[0],"/",novaData[1],"/",novaData[2])
    elif (menu == 3):
        print("\nGerando a data")
        data = geraData()
        print("Você gerou a seguinte data:", data[0], "/", data[1], "/", data[2])
        print("\nGerando a segunda data")
        data2 = geraData()
        print("Você gerou a seguinte data:", data2[0], "/", data2[1], "/", data2[2])
        print("\nAs datas possuem diferença de",diferencaDatas(data,data2),"dia(s)")
    elif (menu != 4):
        print("\nNúmero Inválido!")

print("\nPrograma Encerrado")


