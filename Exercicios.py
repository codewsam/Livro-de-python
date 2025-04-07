L = [15,7,27,39] #numeros possiveis
p = int(input("digite o valor a procurar ")) #input q vc digita o numer q procura
achou = False
x = 0 #posição iniciando em 0

while x < len(L):
    if L[x] == p:
        break
    x+=1
if x<len(L):
    print(f"achou na posição {x+1}")
else:
    print("nao achou")