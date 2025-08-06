#Revisão de Python
print("Olá Mundo!")

''''
Comentários em bloco
Vários comentários
'''

#Tipos de dados
texto = "Tipo texto"
inteiro = 1
flutuante = 1.1
verdadeiro = True #boolean
falso = False #boolean
print(type(texto))
print(type(inteiro))
print(type(flutuante))
print(type(verdadeiro))
print(type(falso))

nome = "Augusto"
idade = 24

#Concatenação e interpolação
print("Meu nome é " + nome + " e tenho " + str(idade) + " anos.")
print(f"Meu nome é {nome} e tenho {idade} anos.")

#Operadores
print(1 + 1)
print(1 - 1)
print(1 * 1)
print(1 / 1)
print(20 % 2)
print(1 ** 1)
print(1 // 1)

#Operadores de atribuição
x = 1
x += 1 #x = x + 1
x -= 1 #x = x - 1
x *= 1 #x = x * 1
x /= 1 #x = x / 1

#Operadores de comparação
print(1 == 1)
print(1 != 1)
print(1 > 1)
print(1 < 1)
print(1 >= 1)
print(1 <= 1)

#Operadores lógicos
print(1 and 1) #&&
print(1 or 1) #||
print(not 1) #!

#Condicionais: if - elif - else
def maioriodade(idade):
    if idade >= 18:
        print("Adulto")
        return
    
    if idade < 18 and idade >= 12:
        print("Adolescente")
        return
    
    print("Crianca")

maioriodade(17)

idade = 18
if idade >= 18:
    print("Adulto")
elif idade < 18 and idade >= 12:
    print("Adolescente")
else:
    print("Crianca")

#Estrutura de repetição: for - while
print("====================")
lista = ["Ana", "Joao", "Maria"]
for i in range(len(lista)):
    print(lista[i])
print("====================")
for nome in lista:
    print(nome)

for i, nome in enumerate(lista):
    print(f"Posição: {i} - Nome: {nome}")

'''
while True:
    x = input("Digite algo: ")
    if x == "sair":
        break
'''
x = 0;
while x < 10:
    print(x)
    x += 1


lista = [1, 2, "teste", 2.1, True]
lista.append("augusto")

for i, valor in enumerate(lista):
    if type(valor) == str:
        lista.pop(i)

print(lista)

#Funções

#Funções sem retorno
def saudacao(nome):
    print(f"Olá, {nome}")

#Funções com retorno
def soma(a, b):
    return a + b

soma(1, 2)

#Funções lambda
somatorio = lambda a, b: a + b
print(somatorio(1, 2))

#Dicionarios
dicionario = {
    "nome": "Augusto",
    "idade": 24
}

dicionario.update({
    "nome": "Augusto Ortolan"
})

print(dicionario.get("nome"))
print(dicionario["idade"])