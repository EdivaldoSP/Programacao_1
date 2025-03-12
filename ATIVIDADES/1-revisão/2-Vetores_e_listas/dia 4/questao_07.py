vetor1 = []
vetor2 = []
vetor3 = []

for i in range(10):
    num = int(input("Digite um número: "))
    vetor1.append(num)

print()
print("Criando o segundo vetor")
print()

for i in range(10):
    num = int(input("Digite um número: "))
    vetor2.append(num)

for i in range(len(vetor1)):
    n1 = vetor1[i]
    vetor3.append(n1)
    
    n2 = vetor2[i]
    vetor3.append(n2)

print(vetor3)