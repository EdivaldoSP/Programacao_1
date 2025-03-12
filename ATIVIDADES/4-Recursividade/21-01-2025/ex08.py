def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n - 1) + f(n - 2)

valorA = int(input("Valor a: "))
valorB = int(input("Valor b: "))
quantidade = int(input("Quantidade: "))

for i in range(quantidade):
    print(f(valorA))
    valorA += 1 