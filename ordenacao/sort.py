
#Método por troca
def bubble_sort(lista):
    if len(lista) <= 1:
            return list

    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(0, len(lista)-1):
            #lista[i] > lista[i+1]
            if lista[i] > lista[i+1]:
                #faz a troca (swap)
                #print(lista[i], lista[i+1])
                lista[i], lista[i+1] = lista[i+1], lista[i]
                ordenado = False #mantém o FALSE sempre que for preciso fazer uma troca de valores
    
    return lista

#Método por inserção
def insertion_sort(lista):
    if len(lista) <= 1:
        return list

    print(f"Lista original: {lista}")
    for i in range(1, len(lista)):
        for j in range(0, i):
            if lista[j] > lista[i]:
                #troca (swap)
                print(f"Troca: {lista[j]} por {lista[i]}")
                lista[j], lista[i] = lista[i], lista[j]

    return lista


#Método por intercalação
def merge(listaEsquerda, listaDireita):
    resultado = []
    i = j = 0 #atribui o mesmo valor para duas variáveis diferentes

    while i < len(listaEsquerda) and j < len(listaDireita):
        if listaEsquerda[i] <= listaDireita[j]:
            resultado.append(listaEsquerda[i])
            i += 1
        else: 
            resultado.append(listaDireita[j])
            j += 1

    # adiciona o que sobrou da esquerda
    resultado.extend(listaEsquerda[i:])

    #adiciona o que sobrou da direita
    resultado.extend(listaDireita[j:])

    return resultado
        

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    #Divide a lista no meio
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    print(f"Esquerda: {esquerda}")
    direita = merge_sort(lista[meio:])
    print(f"Direita: {direita}")

    return merge(esquerda, direita)


def busca_menor_dado(lista, inicio=0):
    menor = inicio #armazena o menor indicie

    for i in range(inicio, len(lista)):
        if lista[i] < lista[menor]:
            menor = i
    
    print(f"Menor: {menor}, Inicio:  índice{inicio} valor {lista[inicio]}")
    return menor #retorna o menor indice da lista

#Método por seleção
def selection_sort(lista):
    print(f"Lista original: {lista}")
    for i in range(0, len(lista)):
        indice_menor = busca_menor_dado(lista, i)
        lista[indice_menor], lista[i] = lista[i], lista[indice_menor]
    
    return lista

#[10, 5, 3, 6, 1, 9]


# print(bubble_sort([5, 2, 10, 3, 6]))
# print(insertion_sort([11, 4, 7, 2, 1, 9, 10]))
# print(merge_sort([10, 5, 3, 6, 1, 9]))
# print(selection_sort([10, 5, 3, 6, 1, 9]))