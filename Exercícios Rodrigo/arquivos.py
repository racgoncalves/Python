# EX 1
'''
with open("exercicio.txt",'w') as arquivo:
    arquivo.write("aprendendo")

with open("exercicio.txt",'a') as arquivo:
    arquivo.write("\nvamos nessa")

with open("exercicio.txt",'r') as arquivo:
    print(arquivo.read())

with open("exercicio.txt",'r') as arquivo:
    print(arquivo.readlines())
'''
# EX 2
'''
with open("exercicio.html",'w') as pagina:

    pagina.write("<body><h1> TESTANDOOO </h1>")
    pagina.write("<br><h2> Escreva um nome </h2>")
    pagina.write("<br><h3>Nomes: ")
    nome = ""
    while nome != "SAIR":
        nome = input("Digite um nome ou 'SAIR': ").upper()
        if nome != "SAIR":
            pagina.write("<br>"+nome)
    pagina.write("</h3></body>")
'''
# EX 3
'''
def registra(dicionario):

    resposta = 'S'

    while resposta == 'S':

        chave = input("Digite o código do país: ")

        dicionario[chave] = [input("Digite o país: "),
                             input("Digite o estado: "),
                             input("Digite a cidade: ")]

        resposta = input("Digite 'S' para continuar: ").upper()


def escreve(dicionario):

    with open("exercicio.csv","a") as arquivo:

        for chave , objeto in dicionario.items():
            arquivo.write(chave + ";" + objeto[0] + ";" + objeto[1] + ";" + objeto[2] + "\n")

        dicionario.clear()
        print("Dicionário escrito no arquivo")


def exibirFind():

    with open("exercicio.csv",'r') as arquivo:

        for linhas in arquivo.readlines():
            separar = linhas[linhas.find(";")+1:-1]
            pais = separar[0:separar.find(";")]
            separar = separar[separar.find(";")+1:-1]
            estado = separar[0:separar.find(";")]
            cidade = linhas[linhas.rfind(";")+1:-1]
            
            print("\nPaís:", pais)
            print("Estado:", estado)
            print("Cidade:", cidade)


def exibir():

    with open("exercicio.csv",'r') as arquivo:
        for linhas in arquivo.readlines():
            lista = linhas.split(";")

            print("\nID:",lista[0],
                "\nPaís:",lista[1],
                "\nEstado:",lista[2],
                "\nCidade:",lista[3])

def limpar():

    with open("exercicio.csv",'w') as arquivo:
        arquivo.write("")
        print("Arquivo Zerado!!!")

def menu():

    num = int(input("\nDigite:"
            "\n1 para registrar"
            "\n2 para escrever no arquivo"
            "\n3 para exibir o que tem no arquivo"
            "\n4 para exibir usando o .find"
            "\n5 para zerar o arquivo"
            "\n6 para sair: "))

    if num < 1 or num > 6:
        print("Número inválido")
        num = menu()

    return num


dicionario = {}
num = menu()

while num > 0 and num < 6:

    if num == 1: registra(dicionario)
    if num == 2: escreve(dicionario)
    if num == 3: exibir()
    if num == 4: exibirFind()
    if num == 5: limpar()

    num = menu()

print("\nPrograma encerrado")
'''
# EX 4
'''
with open("economic-indicators.csv",'r') as arquivo:

    totalVoos = 0
    menorPassageiro = 100000000

    for linha in arquivo.readlines()[1:-1]:
        lista = linha.split(",")

        if int(lista[0]) == 2013:
            totalVoos += int(lista[3])

        if menorPassageiro > int(lista[2]):
            menorPassageiro = int(lista[2])
            ano = lista[0]
            mes = lista[1]

    print("Total de voos de 2013:",totalVoos)
    print("Menor quantidade de passageiros:",
          menorPassageiro,"no mês de",
          mes,"do ano de",ano)
'''