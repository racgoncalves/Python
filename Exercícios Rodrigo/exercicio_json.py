import json
import os

def menu():
    num = int(input("\nDigite"
                      "\n1 para registrar ativo"
                      "\n2 para exibir ativos armazenados"
                      "\n3 para sair: "))
    if num < 1 or num > 3:
        print("Número inválido")
        num = menu()

    return num

def gravar(dicionario, arquivo):
    resp = "S"

    while resp == "S":

        chave = input("Digite o ID: ")
        dicionario[chave] = [
            input("Digite o nome: "),
            input("Digite o sobrenome: ")]
        resp = input("Digite 'S' para continuar: ").upper()

    with open(arquivo,'w') as arq_json:
        json.dump(dicionario, arq_json)
        print("Arquivo gravado!!")

def mostrar(arquivo):

    with open(arquivo,'r') as arq_json:

        carregar = json.load(arq_json)

        for chave , objeto in carregar.items():
            print("\nID:",chave,
                  "\nNome:",objeto[0],
                  "\nSobrenome:",objeto[1])

def ler(arquivo):

    if os.path.exists(arquivo):
        with open(arquivo,'r') as arq_json:
            dicionario = json.load(arq_json)

    else: dicionario = {}

    return dicionario

dicionario = ler("json.json")

num = menu()

while num > 0 and num < 3:

    if num == 1: gravar(dicionario,"json.json")
    if num == 2: mostrar("json.json")

    num = menu()

print("Programa encerrado!!")