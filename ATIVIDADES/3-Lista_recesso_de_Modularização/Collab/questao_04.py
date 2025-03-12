num = int(input("Digite: "))
lista = []


def par_impar(num):
    while num > 1:
        if num % 2 ==0:
            num = num // 2
            lista.append(num)
        
        else:
            num = (num * 3) + 1
            lista.append(num)
       
    return lista
print(par_impar(num))