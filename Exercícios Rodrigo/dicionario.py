# EX 1
'''
dicionario  = { "onix":["pequeno","4 portas","0km"],
                "hilux":["grande","4 portas","100km"]}

dicionario["hilux"]=["grande","2 portas"]

print(dicionario)

print(dicionario.get("hilux"))
'''
# EX 2
'''
resposta = 'S'
nomes = []
chave = {}

while resposta == 'S':
    nomes.append(input("Digite o nome a ser cadastrado: "))
    resposta = (input("Digite 'S' para continuar: ")).upper()

tupla = list(enumerate(nomes))

for item in range(0,len(tupla)):

    print("Nome:",tupla[item][1])
    chave[tupla[item]] = [input("Digite o sobrenome: ")]

print(chave)
'''

# EX 3

def inserir(dicionario):

    def porta():
        quantidadePorta = int(input("Digite a quantidade de portas(2 ou 4): "))
        while quantidadePorta != 2 and quantidadePorta != 4:
            print("Só pode ser 2 ou 4")
            quantidadePorta = int(input("Digite a quantidade de portas(2 ou 4): "))
        return quantidadePorta

    def potencia():
        valorPotencia = float(input("Digite a potência(1.0 a 3.6): "))
        while valorPotencia < 1.0 or valorPotencia > 3.6:
            print("Potencia só pode ser entre 1.0 e 3.6")
            valorPotencia = float(input("Digite a potência(1.0 a 3.6): "))
        return valorPotencia


    resposta = 'S'

    while resposta == 'S':

        chave = input("Digite o modelo do carro: ")

        dicionario[chave] = [input("Digite a marca do carro: "),
                             input("Digite o nome do carro: "),
                             porta(),
                             potencia()]

        resposta = input("Digite 'S' para continuar inserindo: ").upper()

def pesquisa(dicionario):

    objeto = dicionario.get(input("Digite o modelo do carro para pesquisar: "))

    if objeto == None: print("Modelo inexistente")
    else: print("\nMarca:", objeto[0],
              "\nNome:", objeto[1],
              "\nNúmero de portas:", objeto[2],
              "\nPotência:", objeto[3])

def excluir(dicionario):

    chave = input("Digite o modelo do carro a ser excluído: ")

    objeto = dicionario.get(chave)

    if objeto == None:
        print("Modelo inexistente")
    else:
        del dicionario[chave]
        print("Modelo excluído!!")

def limpar(dicionario):

    dicionario.clear()
    print("Dicionário limpo!!")

def listar(dicionario):

    for chave, objeto in dicionario.items():

        print("\nModelo do carro:",chave,
              "\nMarca:", objeto[0],
              "\nNome:", objeto[1],
              "\nNúmero de portas:", objeto[2],
              "\nPotência:", objeto[3])

    for objeto in dicionario.values():

        print("\nMarca:", objeto[0],
              "\nNome:", objeto[1],
              "\nNúmero de portas:", objeto[2],
              "\nPotência:", objeto[3])

    for chave in dicionario.keys():

        print("\nModelo do carro:",chave)

def menu():

    num = int(input("\nDigite:"
                    "\n1 para inserir carro"
                    "\n2 para pesquisar carro"
                    "\n3 para excluir carro"
                    "\n4 para limpar dicionário"
                    "\n5 para listar tudo"
                    "\n6 para fechar programa: "))
    if num < 1 or num > 6:
        print("Número inválido")
        num = menu()

    return num

dicionario = {}

num = menu()

while num > 0 and num < 6:

    if num == 1: inserir(dicionario)
    if num == 2: pesquisa(dicionario)
    if num == 3: excluir(dicionario)
    if num == 4: limpar(dicionario)
    if num == 5: listar(dicionario)

    num = menu()


