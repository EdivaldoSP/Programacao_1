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

texto_exemplo = "A dog and a cat. A frog and a cat."

saida = pre_processamento(texto_exemplo)
#print(saida) # ⭢ [['dog', 'and', 'cat'], ['frog', 'and', 'cat']]

#------------------------------->                 <>                 <-------------------------------|
                        # FUNÇÃO QUE CALCULA O PRODUTO E A SOMA DO DENOMINADOR

def produto_e_soma(vetor):
  total = 0

  for i in range (len(vetor)):
    total += vetor[i] ** 2
  return total

#------------------------------->                 <>                 <-------------------------------|
                        # FUNÇÃO QUE CALCULA A SIMILARIDADE ENTRE AS SENTENÇAS

def similaridade (sentenca1, sentenca2):
  tokens_unicos = list(set(sentenca1 + sentenca2))
  print(tokens_unicos)

  vetor1 = [0] * len(tokens_unicos) # sentença 1
  vetor2 = [0] * len(tokens_unicos) # sentença 2

  for token in sentenca1:
    vetor1[tokens_unicos.index(token)] +=1

  for token in sentenca2:
    vetor2[tokens_unicos.index(token)] +=1

  numerador = 0

  for i in range(len(tokens_unicos)):
    numerador += vetor1[i] * vetor2[i]

  denominador = 0

  variavel_a = produto_e_soma(vetor1)
  variavel_b = produto_e_soma(vetor2)

  denominador = sqrt(variavel_a) * sqrt(variavel_b)
                 
  conseno = numerador / (denominador)
  return conseno

# |=============================================[ x ]=================================================|

#similaridade(saida[0], saida[1])

# calcular a similaridade
