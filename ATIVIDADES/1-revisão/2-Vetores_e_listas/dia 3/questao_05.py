import math

inteiros = []

raiz_quadrada = []

for i in range(5):
    num = int(input("Digite: "))

    if num > 0:
        inteiros.append(num)

for i in range(len(inteiros)):
    raiz = math.sqrt(inteiros[i])
    raiz_quadrada.append(raiz)

print(raiz_quadrada)