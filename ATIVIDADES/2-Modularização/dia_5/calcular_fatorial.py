lista_fat = []

def fatorial (numero):
    fat = 1
    c = 1
    while c <= numero:
        fat = fat * c
        c = c + 1
    return fat

for i in range(5):
    n = int(input("Digite um número: "))
    resposta = fatorial(n)
    lista_fat.append(resposta)
    
for i in range(len(lista_fat)):
    print(f"{i+1} != {lista_fat[i]}, ")