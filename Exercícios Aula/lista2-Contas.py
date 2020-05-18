#lista 2

#ex2
'''
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

print(sobrenome,nome)
'''

#ex3
'''
nome = input("Digite seu nome: ")
nascimento = int(input("Digite o seu ano de nascimento: "))
idade = 2020 - nascimento

print(nome,"tem ou terá",idade,"anos")
'''

#ex4
'''
num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite outro número inteiro:"))

soma = num1 + num2
multiplicacao = num1 * num2
divisao = num1 / num2
resto = num1 % num2

print("soma:",soma,"multiplicação:",multiplicacao,"divisão:",round(divisao,2),"resto:",resto)
'''

#ex5
'''
num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite outro número inteiro:"))

potencia = num1**num2

print("O número",num1,"elevado ao número",num2,'é',potencia)
'''

#ex6
'''
raio = int(input("Digite o raio o círculo em cm: "))

area = raio * raio * 3.141592
perimetro = 2 * raio * 3.141592

print("A área do círculo é",area,"cm² e o perímetro é",perimetro,"cm")
'''

#ex7
'''
num = int(input("Digite um número inteiro entre 0 e 99: "))

if num<0 or num >99:
   print("Número inválido")
else:
    dezena = int(num/10)
    unidade = (num%10)
    print("O número da dezena é:",dezena,"e o número da unidade é:",unidade)
'''

#ex8
'''
x = int(input("Digite o número de camisas: "))
y = int(input("Digite o número de calças: "))
z = int(input("Digite o número de pares de sapatos: "))

combinacoes = x*y*z

print("O número de combinações possíveis é:",combinacoes)
'''

#ex9
'''
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite a % de desconto: "))
desconto = desconto/100

valor_desconto = preco * desconto
novo_preco = preco - valor_desconto

print("Com desconto de:",valor_desconto,"reais o preço do produto fica",novo_preco,"reais e caso "
      "fosse um aumento seria:",preco+valor_desconto,"reais")
'''

#ex10
'''
distancia = float(input("Digite a distância em metros: "))
tempo = int(input("Digite o tempo em segundos: "))

v_media = distancia / tempo
v_km = v_media * 3.6

print("A velocidade média foi de:",round(v_media,2),"m/s ou de:",round(v_km,2),"km/h")
'''

#ex11
'''
salario_antigo = float(input("Digite o antigo salário de João: "))
salario_novo = float(input("Digite o novo salário de João: "))

aumento = ((salario_novo - salario_antigo) / salario_antigo) * 100

print("O percentual de aumento foi de:",round(aumento,2),"%")
'''

#ex12
'''
rm = int(input("Digite o seu RM: "))
soma = 0

while (rm > 0):

    resto = rm % 10
    rm = (rm - resto)/10
    soma = soma + resto

print("A soma dos números do seu RM é:", int(soma))
'''

#ex13
'''
nota_nac = float(input("Digite a nota da NAC: "))*2
nota_am = float(input("Digite a nota da AM: "))*3
nota_ps = float(input("Digite a nota da PS: "))*5

media = (nota_nac + nota_am + nota_ps) / 10

print("A média do aluno foi de:",round(media,2))
'''

#ex14
'''
print("O IPTU poderá ser pago à vista ou em 10 parcelas.")
vista = float(input("Digite o valor total do seu IPTU à vista: "))
parcela = float(input("Digite o valor da parcela de seu IPTU: "))

parcela_total = parcela * 10

if vista > parcela_total:
    print("Valores incorretos, o valor à vista não pode ser maior do que o valor das 10 parcelas somadas.")
else:
    desconto = parcela_total - vista
    desconto_porc = (desconto / parcela_total) * 100
    print("O desconto para o pagamento à vista é de:",round(desconto_porc,2),"%")
'''