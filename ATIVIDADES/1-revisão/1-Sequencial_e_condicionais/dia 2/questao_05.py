import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o vaor de b: "))
c = int(input("Digite o vaor de c: "))

if a != 0:
    delta = (math.pow(b, 2)) - (4 * a * c)

    

    if delta >= 0:
        x1 =  (- b + math.sqrt(delta)) / (2 * a)
        x2 =  (- b - math.sqrt(delta)) / (2 * a)

        print(f"O valor do x1: {x1}")
        print(f"O valor do x2: {x2}")

    if delta == 0:
        x = (- b) / (2 * a)
        print(f"Raiz única: {x}")
    
    if delta < 0:
        print("Não existe raiz")

else:
    print("Não é uma equação do 2º grau")

