paozinho = 0.82
broa = 2.5

quantidade_paes = int(input("Digite a quantidade de pães vendidos: "))
quantidade_broas = int(input("Digite a quantidade de broas vendidos: "))

total_arrecadado = (quantidade_broas * broa) + (quantidade_paes * paozinho)
poupanca = (10 * total_arrecadado) / 100

print(f"O valor arrecadado na vendas de pãozinhos e broas é de: R$ {total_arrecadado}")
print(f"O valor para a poupança é: R$ {poupanca}")