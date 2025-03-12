# entrada = int(input("Digite o valor inicial: "))

# cem = entrada // 100
# cinquenta = entrada // 50
# vinte = entrada / 20
# dez = entrada / 10
# cinco = entrada % 5
# dois = entrada % 2
# um = entrada

#saida = [cem, cinquenta, vinte, dez, cinco, dois, um]

# Abrindo o arquivo em modo de escrita ("w" sobrescreve o conteúdo se já existir)
diretorio = "atividade7/notas.txt"
diretorio2 = "revisao_atividade_avaliativa/atividade7/notas.txt.py"
diretorio3 = "Documents/programacao_1/revisao_atividade_avaliativa"

with open (diretorio3, "w", encoding="utf-8") as arquivo:
    arquivo.write("Esta é a primeira linha do arquivo.\n")
    arquivo.write("Segunda linha de notas.\n")
    arquivo.write("Terceira linha adicionada ao arquivo.\n")

print("Arquivo 'notas.txt' criado com sucesso!")


# with open ("notas.txt", "w", encoding ="UTF-8") as arquivo:
#     for i in saida:
#         arquivo.write(i + "\n")