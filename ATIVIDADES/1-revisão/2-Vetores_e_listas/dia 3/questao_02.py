lista_main = []
lista_negativo = []
lista_positivo = []

soma_negativo = 0
# quantidade_positivo = len(lista_positivo)

for i in range(10):
    num = int(input("Digite: "))

    lista_main.append(num)

    if num > 0:
        lista_positivo.append(num)
    else:
        lista_negativo.append(num)


print(f"Quantidade de números positivos: {len(lista_positivo)}")
print(f"A soma dos números negativos: {soma_negativo}")

for i in range(len(lista_main)-1, 0, -1):
    print(lista_main[i])