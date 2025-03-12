#este código contém erros

def verPrimo (n):
	contador=0
	for i in range (1, n+1):
		if n%i==0:
			contador+=1
	if contador==2:
		return True
	else:
		return False

#entrada de dados

lista=[]
for i in range (9):
	n= int(input("Digite: "))
	lista.append(n)


for i in range (len(lista)):
	if verPrimo (lista[i])==True:
		print (lista[i], i)
