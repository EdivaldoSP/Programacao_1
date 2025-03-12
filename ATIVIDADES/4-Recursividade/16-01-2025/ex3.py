vetor = [1, 2, 3, 4, 5]

def somar_elementos(vetor):
    if not vetor:
        return 0
    else:
        return vetor[0] + somar_elementos(vetor[1:])
   
# RECURSIVIDADE
# 1º rodada = 1 + (2, 3, 4, 5) = somar_elementos(vetor[1:])
# 2º rodada = 2 + (3, 4, 5) = somar_elementos(vetor[1:])
# 3º rodada = 3 + (4, 5) = somar_elementos(vetor[1:])
# 4º rodada = 4 + (5) = somar_elementos(vetor[1:])
# 5º rodada = 5 + (0) caso base

# PILHAS 
# 5 + 0 = 5
# 5 + 4 = 9
# 9 + 3 = 12
# 12 + 2 = 14
# 14 + 1 = 15