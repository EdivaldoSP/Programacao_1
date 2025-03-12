dias  = int(input("Digite os dias trabalhados: "))
salario = dias * 90
desconto = (8 * salario) / 100

salario_liquido = salario - desconto
print(f"A quantia líquida a ser paga ao encandor é de : {salario_liquido}")
