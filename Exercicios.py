L = [15,7,27,39]
p = int(input("digite o valor a procurar "))
achou = False
x = 0

while x < len(L):
    if L[x] == p:
        achou = True
        break
    x+=1
if achou:
    print(f"achou na posição {x}")
else:
    print("nao achou")