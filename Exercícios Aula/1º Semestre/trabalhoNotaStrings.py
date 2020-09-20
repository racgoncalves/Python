
def contaVogal(string):
    cont = 0
    for i in range(0,len(string)):
        if(string[i]=="a" or string[i]=="e" or string[i]=="i" or string[i]=="o" or string[i]=="u"):
            cont += 1
    return cont

def inverteString(string):
    n = 0
    string2 = ""
    while (len(string)-n > 0):
        string2 += string[len(string)-1-n]
        n += 1
    return string2

string = input("Digite um texto: ")
print("O número de vogais no seu texto é:",contaVogal(string))
print("O texto invertido é:",inverteString(string))

