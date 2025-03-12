def para_baixo (numero):
    num_real = numero - int(numero)
    num_int = int(numero)
    return num_int

def para_cima (numero):
    num_real = numero - int(numero)
    num_int = int(numero)

    if num_real >= 0:
        resultado = num_int + 1
        return resultado
    else:
        print("ERRO")
    

def convencional (numero):
    num_real = numero - int(numero)
    num_int = int(numero)

    if num_real >= 0.5:
        resultado = num_int + 1
        return resultado
    else:
        resultado = num_int
        return resultado

num = float(input("Digite um número real não negativo: "))

calculo1 = para_baixo(num)
calculo2 = para_cima(num)
calculo3 = convencional(num)

print(calculo1)
print(calculo2)
print(calculo3)