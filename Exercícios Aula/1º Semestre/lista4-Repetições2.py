
#exercício 1
'''
import random

sorteado = random.randint(1,1001)

num = 0
tent = 0

while num != sorteado:
    num = int(input("Tente advinhar o número sorteado: "))
    tent += 1
    if num > sorteado:
        print("Seu número está MAIOR do que o sorteado")
    elif num < sorteado:
        print("Seu número está MENOR do que o sorteado")

print("Parabéns, você acertou o número sorteado:",sorteado)
print("Quantidade de tentativas:",tent)
'''

#exercício 2
'''
num = 0

while num <= 0:
    num = int(input("Digite um número inteiro e positivo para testar se é perfeito: "))
    if num <= 0:
        print("O número deve ser positivo")

i = 1
soma = 0

while i < num:
    if num % i == 0:
        soma += i
    i += 1

if soma == num:
    print("O número",num,"é perfeito")
else:
    print("O número", num, "NÃO é perfeito")
'''

#exercício 3
'''
lista = []
lista1 = [5,10,3,2,4,7,9,8,5]
lista2 = [10,8,7,5,2]
lista3 = []
listaSeq = []
add = 0
resp = 0
resp2 = "S"
crescente = 1

while resp != 1 and resp != 2 and resp != 3:
    print("1 -",lista1,"\n2 -",lista2,"\n3 - criar sua própria lista")
    resp = int(input("Digite a opção desejada: "))
    if resp == 1: lista = lista1
    elif resp == 2: lista = lista2
    elif resp == 3:
        add = int(input("Digite um número inteiro para adicionar à lista: "))
        lista3.append(add)
        while resp2 == "S":
            add = int(input("Digite outro número inteiro para adicionar à lista: "))
            lista3.append(add)
            resp2 = input("Digite 'S' para continuar adicionando elementos à lista ou qualquer outro caractere para sair: ").upper()
        lista = lista3

for i in range(0,len(lista)-1):
    if lista[i] < lista[i+1]:
        crescente += 1
    if lista[i] >= lista[i+1] or i+1 == len(lista)-1:
        listaSeq.append(crescente)
        crescente = 1

print("Na sequência",lista,"o comprimento do segmento crescente máximo é",max(listaSeq))
'''

#exercício 3 Professor
'''
n = int(input("Informe tamanho da seq: "))

ant = int(input("Digite num da seq: "))
comp = 1

contador = 1

maior = 1

while contador < n:
    atual = int(input("Digite num da seq: "))
    contador = contador + 1
    if ant < atual:
        comp = comp + 1    
    else:
        comp = 1    

    if comp > maior:
        maior = comp

    ant = atual

print("O comprimento do segmento cresc maximo e", maior)
'''

