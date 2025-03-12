import nltk

from math import *
from nltk.tokenize import word_tokenize
from nltk import FreqDist
from nltk.corpus import stopwords

# nltk.download('punkt_tab') # Usado na tokenização
# nltk.download('stopwords') # Módulo para stopwords
# nltk.download('rslp') # Módulo para radicalizar
# nltk.download('averaged_perceptron_tagger_eng')


# FAZENDO A LEITURA DO ARQUIVO .TXT

with open ("Colab-2/texto2.txt", "r", encoding="UTF-8") as arquivo:
    texto1 = arquivo.read()
    #print(texto1)

with open ("Colab-2/mariele.txt", "r", encoding="UTF-8") as arquivo:
    mariele_texto = arquivo.read()
    #print(texto2)

# FUNÇÃO QUE FAZ O PRE-PROCESSAMENTO DO ARQUIVO .TXT

def pre_processamento(text):
    sentencas = nltk.tokenize.sent_tokenize(text)

    # NORMALIZANDO AS SENTENÇAS USANDO A FUNCÃO LOWER NATIVA DO PYTHON

    sentencas_normalizadas = []

    for palavra in sentencas:
        minusculas = palavra.lower()
        sentencas_normalizadas.append(minusculas)

    # STOPWORDS

    stopwords = nltk.corpus.stopwords.words("portuguese")

    # REMOVENDO STOPWORDS

    sentencas_limpas = [] # --> setenças sem as stopswords e em lowercase

    for sentenca in sentencas_normalizadas:
        tokens = word_tokenize(sentenca)

        token_limpo = []
        for palavra in tokens:
            if palavra not in stopwords and palavra.isalnum():
                token_limpo.append(palavra)
        sentencas_limpas.append(token_limpo)

    return sentencas_limpas

resultado1 = pre_processamento(texto1)
resultado2 = pre_processamento(mariele_texto)

#print(resultado1)
#print(resultado2)

# OBS: Para ver a explicação com mais detalhes da função "pre_processamento", veja a pasta "colab-1"
# nesse mesmo projeto no github ou acesse o link: ...

# |=============================================[ x ]=================================================|
                                # DESCOBRINDO A FREQUÊNCIA DE CADA TOKEN

lista1 = [t for s in resultado2 for t in s] # --> forma que a professora fez para acessar os tokens 
                                            #     usando a list comprehension

# ↓ a forma que eu fiz para acessar os tokens (os tokens estavam em uma lista e a mesma estava em 
# uma outra lista maior - lista dentro de lista)

lista2 = []
for sentenca in resultado2:
    for token in sentenca:
        lista2.append(token)

#print(lista1)
#print(lista2)


frequencia = FreqDist(lista2)
#print(frequencia.most_common())

# |=============================================[ x ]=================================================|
                                # CONSENO: UMA MEDIDA DE SIMILARIDADE

# A similaridade por cosseno é uma medida da similaridade de entre dois vetores num espaço vetorial que 
# avalia o valor do cosseno do ângulo compreendido entre eles.

# Ela compara as palavras de 2 textos, ignorando a ordem, e cria um vetor com as palavras mais repetidas. 
# Aplica-se a fórmula e o resultado é um valor entre 0 e 1. Quanto mais próximo de 0, menos similares 
# são duas sentenças. Quanto mais próximo de 1, bastante similares são as sentenças.

texto_exemplo = "A dog and a cat. A frog and a cat."

saida = pre_processamento(texto_exemplo)
#print(saida) # ⭢ [['dog', 'and', 'cat'], ['frog', 'and', 'cat']]

#------------------------------->                 <>                 <-------------------------------|
                                # ELIMINANDO TOKENS REPETIDOS DAS SENTENÇAS

tokens_unicos = list(set(saida[0] + saida[1]))

# O que está acontecendo? Vamos por partes.

# 1º ⭢ vamos concatenar as duas sentenças
# 2º ⭢ a função set irá analisar os tokens repetidos e irá eliminá-los, transformando a lista em uma 
# outra estrutura de dados
# 3º ⭢ agora vamos tranformar de volta para lista com a função list.

#rint(tokens_unicos) # ⭢  ['and', 'cat', 'dog', 'frog']

#------------------------------->                 <>                 <-------------------------------|
            # CRIANDO VETORES COM A MESMA QUANTIDADE ZEROS DO TAMANHO DA LISTA "tokens_unicos"

vetor1 = [0] * len(tokens_unicos) # sentença 1
vetor2 = [0] * len(tokens_unicos) # sentença 2

#print(vetor1) # ⭢  [0, 0, 0, 0]
#print(vetor2) # ⭢  [0, 0, 0, 0]

#------------------------------->                 <>                 <-------------------------------|
                            # VERIFICANDO A POSIÇÃO DOS TOKENS DAS SENTENÇAS

# aqui iremos construir os vetores "vetor1" e "vetor2" com novos valores que irão representar a 
# frequência das palavras (tokens) que estão dentro da lista "teste".

# O QUE ESTÁ ACONTECENDO COM O CÓDIGO ABAIXO? 

for token in saida[0]:
    vetor1[tokens_unicos.index(token)] += 1 

# 1º ⭢ estamos acessando cada token na lista "saida" percorrendo com o for.
# 2º ⭢ na primeira repetição, o valor do token é 0, então ele irá acessar a palavra "dog" na lista "saida".
# 3º ⭢ depois que ele acessar a palavra "dog", ele irá verificar em qual posição a palavra ocupa na 
# lista "tokens_unicos"
# 4º ⭢ "dog" ocupa a posição 2 em "tokens_unicos", dessa forma, será acrescentado 1 na mesma posição 
# no vetor1 de zeros.

# O CÓDIGO ABAIXO ESTÁ FAZENDO A MESMA COISA, SÓ QUE COM A OUTRA SENTENÇA DA LISTA "saida"

for token in saida[1]:
    vetor2[tokens_unicos.index(token)] += 1

print(vetor1) # ⭢  [1, 1, 1, 0] exemplo
print(vetor2) # ⭢  [1, 0, 1, 1] exemplo

#------------------------------->                 <>                 <-------------------------------|
                    # CALCULANDO O NUMERADOR E O DENOMINADOR DA FÓRMULA DO CONSENO

# NUMERADOR

numerador = 0

for i in range(len(vetor1)):
    numerador += vetor1[i] * vetor2[i]

#------------------------------->                 <>                 <-------------------------------|
# DENOMINADOR

# obs: essa foi a forma que fiz para testar a lógica sem ter que fazer uma função. No final, tem-se 
# uma função que calcula o produto e a soma dos vetores (quaisquer que seja eles).

total_1 = 0
for i in range(len(vetor1)):
   total_1 += vetor1[i] ** 2

total_2 = 0
for i in range(len(vetor2)):
   total_2 += vetor2[i] ** 2

a = sqrt(total_1)
b = sqrt(total_2)

denominador = a * b

# |=============================================[ x ]=================================================|