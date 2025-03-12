#este código contém erros

lista=[]
for i in range (5):
	n=int(input("Digite: "))
	lista.append(n)


def acharMaior(lista):
	maior=lista[0]

	for i in range (len(lista)):
		if lista[i] > maior:
			maior=lista[i]
    
	return maior

resultado = acharMaior(lista)

print(resultado)