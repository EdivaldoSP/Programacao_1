def somar(n):
    if n==1:
        return 1
    else:
        print("passou com n: ", n)
        resultado = n + somar(n - 1)
        return resultado

num = int(input("Numero: "))
result = somar(num)
print(result)