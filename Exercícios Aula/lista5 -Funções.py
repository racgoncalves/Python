
def checaTamanho(lista, lista2):
    return len(lista) == len(lista2)

def viraLista(num):

    #converte separando unidades e adicionando na lista
    '''
    lista = []
    x = 1
    while x < num:
        u = int((num // x) % 10)
        x *= 10
        lista.append(u)
    return lista
    '''

    #converte usando string, lista e transformando em outra com int

    num = str(num)
    lista = list(num)
    lista2 = []

    for i in range(0,len(lista)):
        aux = int(lista[i])
        lista2.append(aux)
    return lista2

def comparaLista(lista, lista2):
    cont = 0
    i = 0
    comp = len(lista)

    while i < len(lista) and len(lista) > 0:
        k = 0
        while k < len(lista2) and len(lista2) > 0 and len(lista) > 0:
            if (lista[i] == lista2[k]):
                lista.pop(i)
                lista2.pop(k)
                cont += 1
                k = 0
                i = 0
            else:
                k += 1
        i += 1
    return comp == cont

def encaixa(lista,lista2):
    x = len(lista2)-1
    y = len(lista)-1
    cont = 0
    while x >= 0:
        if (lista2[x] == lista[y]):
            cont += 1
        x -= 1
        y -= 1
    return cont == len(lista2)

def menorLista(lista,lista2):
    if (len(lista) < len(lista2)):
        return lista
    else:
        return lista2

def maiorLista(lista,lista2):
    if (len(lista) < len(lista2)):
        return lista2
    else:
        return lista

def segmento(lista,lista2):

    maior = maiorLista(lista,lista2)
    menor = menorLista(lista,lista2)

    k = 0
    cont = 0

    for i in range(0,len(maior)):
        if (maior[i] == menor[k]):
            while (maior[i] == menor[k]):
                cont += 1
                k += 1
                i += 1
                if cont == len(menor):
                    return True
        k = 0
        cont = 0
    return False

def maiorNumero(num,num2):
    if (num > num2):
        return num
    else:
        return num2

def menorNumero(num,num2):
    if (num > num2):
        return num2
    else:
        return num

def testaPerfeito(num):
    i = 1
    soma = 0
    while i < num:
        if num % i == 0:
            soma += i
        i += 1

    if soma == num:
        return num

# Fim das funções

'''
# Mostra números perfeitos
num = int(input("Digite um numero: "))
print("\nOs números perfeitos até",num,"são:")

i = 0

while i < num:
    i += 1
    if(testaPerfeito(i)):
        print(testaPerfeito(i))
'''

num = 0
num2 = 0

while num <= 0:
    num = int(input("Digite um número inteiro positivo: "))
while num2 <= 0:
    num2 = int(input("Digite outro número inteiro positivo: "))

lista = viraLista(num)
lista2 = viraLista(num2)

# Permutação
'''
if (checaTamanho(lista,lista2) and comparaLista(lista,lista2)):
    print("O número",num,"é permutação de",num2)
else:
    print("O número",num,"não é permutação de",num2)
'''

# Encaixa
'''
if (encaixa(lista,lista2)):
    print("O número",num2,"encaixa no número",num)
else:
    print("O número",num2,"não encaixa no número",num)
'''

# Segmento
'''
maior = maiorNumero(num,num2)
menor = menorNumero(num,num2)

if (segmento(lista,lista2)):
    print(menor,"é segmento de",maior)
else:
    print(menor,"não é segmento de",maior)
'''