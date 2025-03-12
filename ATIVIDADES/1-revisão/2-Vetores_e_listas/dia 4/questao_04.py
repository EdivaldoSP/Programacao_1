# FATORIAL

n = 5

vetor_1 = []
vetor_2 = []

resultado = 1

for i in range(5):
    num = int(input("Digite um número: "))
    vetor_1.append(num)

for i in range(len(vetor_1)):
    fat = vetor_1[i] 

    for i in range(fat):
        resultado = resultado * (i+1)

    vetor_2.append(resultado)
    resultado = 1

print(vetor_2)
