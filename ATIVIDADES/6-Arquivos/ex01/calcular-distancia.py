leitura = "ex01\arquivo.txt"
with open (file=leitura,mode='r',encoding='UTF-8') as arq:
    x1 = arq.readline()
    print(x1)
    y1 = arq.readline()
    x2 = arq.readline()
    y2 = arq.readline()
