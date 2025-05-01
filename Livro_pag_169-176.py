#usando o range:
for v in range (2,20,2): #gera de 2 a 20, de 2 em 2
    print(v, end=' ') #argumento end=' ' para não pular linha   
print() #primeiro print para pular linha

print("-------------------------------------------------------------------")
#usando enumerate:
#enumerate gera o índice e o valor
L = [1,2,3,4,5]
for x, y in enumerate(L): #enumerate gera o índice e o valor
    print(f"Posição:{x}, valor:{y}") #imprime o índice e o valor

print("-------------------------------------------------------------------")

#Operações com listas
x = [1,4,7,9]
maximo = x[0] #inicializa o máximo com o primeiro elemento da lista 
for e in x: #para cada elemento e em X
    if e > maximo: #se e for maior que o máximo
        maximo = e #atualiza o máximo   
print(f"Máximo: {maximo}") #imprime o máximo

print("-------------------------------------------------------------------")

#agr o minimo
x = [1,4,7,9]
minimo= x[0] #inicializa o máximo com o primeiro elemento da lista 
for e in x: #para cada elemento e em X
    if e < minimo: #se e for maior que o máximo
        minimo = e #atualiza o máximo   
print(f"Minimo: {minimo}") #imprime o máximo

print("-------------------------------------------------------------------")

print("exercicio 6.13:")
t = [-10,-8,0,1,2,5,-2,-4]
maximo = t[0]
minimo = t[0]

soma = sum(t) #soma todos os elementos da lista
media = soma / len(t) #len diz quantos elementos tem


for e in t: #e serve para percorrer a lista             
        if e > maximo: #se e for maior que o máximo
            maximo = e #atualiza o máximo   
        if e < minimo: #se e for menor que o mínimo
            minimo = e #atualiza o mínimo   
print(f"Máximo: {maximo}") #imprime o máximo   
print(f"Minimo: {minimo}") #imprime o máximo
print(f"media: {media}") #imprime a média

print("-------------------------------------------------------------------")
#listas dentro de listas:
produto_1 = ["banana", 1.50, 10] #nome, preço, quantidade
produto_2 = ["maçã", 2.00, 5] #nome, preço, quantidade 
compras = [produto_1, produto_2] #lista de compras, uma lista dentro da outra  

print(compras) #imprime a lista de compras
print(compras[0]) #imprime o primeiro produto
print(compras[0][0]) #imprime o nome do primeiro produto
print(compras[1][2]) #imprime a quantidade do segundo produto

print("-------------------------------------------------------------------")
