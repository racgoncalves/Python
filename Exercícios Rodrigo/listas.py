# EX 1
'''
lista = []
resposta = 'S'

while resposta == 'S':
    lista.append(input("Digite o elemento a ser adicionado na lista: "))
    resposta = input("Digite 'S' para continuar a adicionar: ").upper()

lista.insert(2,"inclusao")

lista.pop()

print(lista)
'''

# EX 2
'''
lista = []
resposta = 'S'

while resposta == 'S':
    lista.append(int(input("Digite um numero inteiro a ser adicionado na lista: ")))
    resposta = input("Digite 'S' para continuar a adicionar: ").upper()

print("soma:",sum(lista),"maior:",max(lista),"menor:",min(lista))
'''

# EX 3
'''
codigo = []
marca = []
tamanho = []
cor = []
preco = []

resposta = 'S'

while resposta == 'S':
    codigo.append(int(input("Digite o código da roupa: ")))
    marca.append(input("Digite a marca da roupa: "))
    tamanho.append(input("Digite o tamanho da roupa (P,M,G): ").upper())
    cor.append(input("Digite a cor da roupa: "))
    preco.append(float(input("Digite o preço da roupa: ")))

    resposta = input("Digite 'S' para continuar: ").upper()

for mostre in range(0,len(codigo)):
    print("Código:",codigo[mostre],
          "\nMarca:",marca[mostre],
          "\nTamanho:",tamanho[mostre],
          "\nCor:",cor[mostre],
          "\nPreço:",preco[mostre])
'''

# EX 4

def inserir(lista):
    resposta = 'S'

    while resposta == 'S':
        roupa = []
        roupa.append(int(input("Digite o código da roupa: ")))
        roupa.append(input("Digite a marca da roupa: "))
        tamanho = (input("Digite o tamanho da roupa(P, M ou G): ").upper())
        while tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
            tamanho = (input("Digite o tamanho da roupa(P, M ou G): ").upper())
        roupa.append(tamanho)
        roupa.append(input("Digite a cor da roupa: "))
        roupa.append(float(input("Digite o preço da roupa: ")))
        lista.append(roupa)
        resposta = input("Digite 'S' para adicionar outra roupa: ").upper()


def buscar(lista):
    marca = input("Digite a marca que deseja buscar: ")

    for busca in lista:
        if marca == busca[1]:
            print("código:", busca[0])
            print("marca:", busca[1])
            print("tamanho:", busca[2])
            print("cor:", busca[3])
            print("preço:", busca[4])


def desconto(lista):
    marca = input("Digite a marca que receberá 10% de desconto: ")

    for busca in lista:
        if marca == busca[1]:
            print("Código:", busca[0])
            print("Preço antigo", busca[4])
            busca[4] *= 0.9
            print("Novo preço:", busca[4])


def excluir(lista):
    codigo = int(input("Digite o código da roupa que será excluída: "))

    for busca in lista:
        if codigo == busca[0]:
            lista.remove(busca)
            print("Exluído da lista")


def mostrar(lista):
    for busca in lista:
        print("código da roupa:", busca[0])
        print("marca:", busca[1])
        print("tamanho:", busca[2])
        print("cor:", busca[3])
        print("preço:", busca[4])


def menu():
    num = int(input("Digite:"
                    "\n1 para inserir"
                    "\n2 para buscar"
                    "\n3 para descontar 10%"
                    "\n4 para excluir"
                    "\n5 para mostrar tudo"
                    "\n6 para sair: "))
    if num < 1 or num > 6:
        print("Número inválido")
        num = menu()
    return num


lista = []

num = menu()

while num > 0 and num < 6:

    if num == 1:
        inserir(lista)
    if num == 2:
        buscar(lista)
    if num == 3:
        desconto(lista)
    if num == 4:
        excluir(lista)
    if num == 5:
        mostrar(lista)

    num = menu()
