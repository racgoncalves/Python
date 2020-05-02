
def escreve():
    with open("exercicio.csv", "a") as arquivo:

        resposta = 'S'

        while resposta == 'S':
            arquivo.write(input("Digite o código do país: ") + ";"
                          + input("Digite o país: ") + ";"
                          + input("Digite o estado: ") + ";" + input("Digite a cidade: ") + "\n")

            resposta = input("Digite 'S' para continuar: ").upper()

        print("\nAdicionado com sucesso")


def exibirFind():
    with open("exercicio.csv", 'r') as arquivo:
        for linhas in arquivo.readlines():
            separar = linhas[linhas.find(";") + 1:-1]
            pais = separar[0:separar.find(";")]
            separar = separar[separar.find(";") + 1:-1]
            estado = separar[0:separar.find(";")]
            cidade = linhas[linhas.rfind(";") + 1:-1]

            print("\nPaís:", pais)
            print("Estado:", estado)
            print("Cidade:", cidade)


def exibir():
    with open("exercicio.csv", 'r') as arquivo:
        for linhas in arquivo.readlines():
            lista = linhas.split(";")

            print("\nID:", lista[0],
                  "\nPaís:", lista[1],
                  "\nEstado:", lista[2],
                  "\nCidade:", lista[3])


def limpar():
    with open("exercicio.csv", 'w') as arquivo:
        arquivo.write("")
        print("Arquivo Zerado!!!")


def menu():
    num = int(input("\nDigite:"
                    "\n1 para escrever no arquivo"
                    "\n2 para exibir o que tem no arquivo"
                    "\n3 para exibir usando o .find"
                    "\n4 para zerar o arquivo"
                    "\n5 para sair: "))

    if num < 1 or num > 5:
        print("Número inválido")
        num = menu()

    return num

num = menu()

while num > 0 and num < 5:

    if num == 1: escreve()
    if num == 2: exibir()
    if num == 3: exibirFind()
    if num == 4: limpar()

    num = menu()

print("\nPrograma encerrado")