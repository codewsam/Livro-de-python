L = [15,7,27,39] #numeros possiveis
p = int(input("digite primeiro valor a procurar ")) #input q vc digita o numer q procura
s = int(input("digite segundo valor a procurar "))
achou = False
x = 0 #posição iniciando em 0


while x < len(L):
    if L[x] == p:
        break
    x+=1
if x<len(L):
    print(f"achou o segundo na posição {x+1}")
else:
    print("nao achou o primeiro ")

while x < len(L):
    if L[x] == s:
        break
    x+=1
if x<len(L):
    print(f"achou o segundo na posição {x+1}")
else:
    print("nao achou o segundooo")

