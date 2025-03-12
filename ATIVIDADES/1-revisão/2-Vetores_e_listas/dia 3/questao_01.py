n = int(input("Digite: "))

maior = n
menor = n

cont = 0

while n >= 0:
    if cont == 0:
        maior = n
        menor = n
        cont += 1

    n = int(input("Digite: "))
    
    if n > maior:
        maior = n

    if n < menor and n != -1:
        menor = n
    
print(f"maior: {maior}")
print(f"menor: {menor}")