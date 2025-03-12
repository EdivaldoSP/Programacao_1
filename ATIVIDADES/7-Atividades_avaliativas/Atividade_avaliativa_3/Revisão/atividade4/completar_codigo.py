leitura = "atividade4/entrada.txt"
lista = []


def lendo(leitura, lista):
    with open (leitura) as arquivo:
        cont = 0 
        
        for i in arquivo:
            lista.append({})
            
            auxiliar = i.split()

            lista[cont]["produto"] = auxiliar[0]
            lista[cont]["total"] = int(auxiliar[1])
            cont += 1

lendo(leitura, lista)
print(lista)