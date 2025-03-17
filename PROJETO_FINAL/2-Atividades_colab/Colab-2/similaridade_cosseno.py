import nltk
import spacy

nlp = spacy.load("pt_core_news_sm")

from math import *
from nltk.tokenize import word_tokenize
from nltk import FreqDist
from nltk.corpus import stopwords
from collections import Counter

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

with open ("Colab-2/texto_auxiliar.txt")as arquivo:
   programacao = arquivo.read()
  #print(programacao)

# FUNÇÃO QUE FAZ O PRE-PROCESSAMENTO DO ARQUIVO .TXT

def pre_processamento(texto):
    sentencas = nltk.tokenize.sent_tokenize(texto)

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

# resultado1 = pre_processamento(texto1)

resultado2 = pre_processamento(mariele_texto)


#print(resultado2)

# |=============================================[ x ]=================================================|
                                # DESCOBRINDO A FREQUÊNCIA DE CADA TOKEN

lista2 = []
for sentenca in resultado2:
    for token in sentenca:
        lista2.append(token)

frequencia = FreqDist(lista2)
#print(frequencia.most_common())

# |=============================================[ x ]=================================================|
                        # FUNÇÃO QUE CALCULA O PRODUTO E A SOMA DO DENOMINADOR

def produto_e_soma(vetor):
  total = 0

  for i in range (len(vetor)):
    total += vetor[i] ** 2
  return total

#------------------------------->                 <>                 <-------------------------------|
                        # FUNÇÃO QUE CALCULA A SIMILARIDADE ENTRE AS SENTENÇAS

def similaridade (sentencas_limpas):
  lista_das_similaridades = []

  for indice in range(len(sentencas_limpas)-1):
    tokens_unicos = list(set(sentencas_limpas[indice] + sentencas_limpas[indice + 1]))

    vetor1 = [0] * len(tokens_unicos) # sentença 1
    vetor2 = [0] * len(tokens_unicos) # sentença 2

    for token in sentencas_limpas[indice]:
      vetor1[tokens_unicos.index(token)] += 1

    for token in sentencas_limpas[indice + 1]:
      vetor2[tokens_unicos.index(token)] += 1
  #---------------------------------------------------------------------------------------------------#
    numerador = 0

    for i in range(len(tokens_unicos)):
      numerador += vetor1[i] * vetor2[i]

    variavel_a = produto_e_soma(vetor1)
    variavel_b = produto_e_soma(vetor2)

    denominador = sqrt(variavel_a) * sqrt(variavel_b)
                 
    cosseno = numerador / (denominador)
  #---------------------------------------------------------------------------------------------------#
    
    lista_das_similaridades.append(cosseno)

  return lista_das_similaridades

# |=============================================[ x ]=================================================|

def media_sentencas(lista_das_similaridades):
  # achar a media entre as similaridades

  soma_similaridades = 0
  quantidade_similaridades = len(lista_das_similaridades)

  for similaridade_entre_sentencas in lista_das_similaridades:
    soma_similaridades += similaridade_entre_sentencas
    #quantidade_de_similaridades += 1

  media_similaridades = soma_similaridades / quantidade_similaridades

  return media_similaridades

# |=============================================[ x ]=================================================|
# def dicionario(texto):
#   lista_dicionarios = []
  
#   sentencas = nltk.tokenize.sent_tokenize(texto)

#   for i in range(len(sentencas)):
#     dicionario = {}

#     dicionario[f"s{i+1}"] = sentencas[i]
  
#     lista_dicionarios.append(dicionario)

#   return lista_dicionarios

# |=============================================[ x ]=================================================|
def criar_subtopicos(texto, lista_similaridades, media_similaridade):
  sentencas = nltk.tokenize.sent_tokenize(texto)

  sub_topico = []
  sub_topico_atual = [sentencas[0]]

  media = round(media_similaridade, 4) 
  
  for i in range(len(lista_similaridades)):
    if lista_similaridades[i] > media:
      sub_topico_atual.append(sentencas[i + 1])
    
    if lista_similaridade[i] < media:
      sub_topico.append(sub_topico_atual)
      sub_topico_atual = [sentencas[i + 1]]

  return sub_topico

# |=============================================[ x ]=================================================|
def criar_rotulos(lista_de_subtopicos):
  rotulos = []  # Lista para armazenar os rótulos

  for subtopico in lista_de_subtopicos:
    palavras_validas = []  # Lista para armazenar substantivos e verbos

    # Percorre cada sentença do subtópico
    for sentenca in subtopico:
      doc = nlp(sentenca)  # Processa a sentença com spaCy
      for token in doc:
        # Verifica se a palavra é um substantivo (NOUN) ou verbo (VERB)
        if token.pos_ in ["NOUN", "VERB"]:
          palavras_validas.append(token.text.lower())  # Adiciona em minúsculas

    # Conta a frequência das palavras
    contagem = Counter(palavras_validas)

    # Seleciona as 5 palavras mais comuns
    rotulo = [palavra for palavra, _ in contagem.most_common(5)]

    rotulos.append(rotulo)  # Adiciona o rótulo à lista de rótulos

  return rotulos  # Retorna a lista com os rótulos de cada subtópico

  # palavras_validas = []

  # # Percorre cada sentença do subtópico
  # for subtopico in sub_topicos:

  #   for sentenca in subtopico:
  #     doc = nlp(sentenca)  # Processa a sentença com spacy

  #     for token in doc:
  #       # Verifica se a palavra é um substantivo (NOUN) ou verbo (VERB)
  #       if token.pos_ in ["NOUN", "VERB", "ADJ", "PROPN"]:
  #         palavras_validas.append(token.text.lower())  # Adiciona em minúsculas

  # # Conta a frequência das palavras
  # contagem = Counter(palavras_validas)

  # # Seleciona as 5 palavras mais comuns
  # rotulo = [palavra for palavra, _ in contagem.most_common(5)]

  # return rotulo  # Retorna a lista com o rótulo do subtópico

# def criar_rotulos(sub_topicos):
#   rotulos_subtopicos = []

#   for subtopico in sub_topicos:
#     string_subtopico = ' '.join(subtopico)

#     doc = nlp(string_subtopico)

#     palavras_relevantes = []

#     for token in doc:
#       if token.pos_ in ["NOUN", "VERB", "ADJ", "PROPN"] and not token.is_stop:
#         palavras_relevantes.append(token.text)
    
#     frequencia = FreqDist(palavras_relevantes)
#     palavras_mais_frequentes = frequencia.most_common(5)

#     palavras_extraidas = []

#     for palavra, contagem in palavras_mais_frequentes:
#         palavras_extraidas.append(palavra)

#     rotulo = ' '.join(palavras_extraidas)

#     rotulos_subtopicos.append(rotulo)

#   return rotulos_subtopicos

  # |============================================[ x ]================================================|

  # for sentenca in resultado2:
  #     for token in sentenca:
  #       if ...
  #         palavras_revelantes.append(token)

  # doc = nlp(sub_topicos)

  # frequencia = FreqDist(doc)
  # result = frequencia.most_common()

  

#print(frequencia.most_common())


# |=============================================[ x ]=================================================|

# resultado_similaridade1 = similaridade(resultado3)

# media = media_sentencas(resultado_similaridade1)

# teste = juntar_sentencas(programacao, resultado_similaridade1, media)

# teste2 = dicionario(programacao)
# |=============================================[ x ]=================================================|

# texto = "Python é uma linguagem popular para ciência de dados."
# doc = nlp(texto)  # Processa o texto

# print(doc) # é uma lista com varios tokens

# for token in doc:
#   print(token.text, token.pos_)  # Exibe a palavra e sua classe gramatical

# palavras_relevantes1 = []

# for token in doc:
#   if token.pos_ in ["NOUN", "VERB"]:
#     palavras_relevantes1.append(token.text)

# print(palavras_relevantes1)
# print(palavras_relevantes2)

# |=============================================[ x ]=================================================|

resultado3 = pre_processamento(programacao)
lista_similaridade = similaridade(resultado3)
media_lista = media_sentencas(lista_similaridade)

subtopicos = criar_subtopicos(programacao, lista_similaridade, media_lista)
#rotulos = criar_rotulos(subtopicos)
rotulos_gerados = criar_rotulos(subtopicos)

print("-" * 170)
print("PROCESSAMENTO: ")
print(resultado3)
print(len(resultado3))
# print(len(teste2))


print("-" * 170)
print("LISTA DAS SIMILARIDADES: ")
print(lista_similaridade)
print(len(lista_similaridade))

print("-" * 170)
print("MEDIA DAS SIMILARIDADES: ")
print(media_lista)

print("-" * 170)
print("SUBTOPICOS: ")
print(subtopicos)

print("-" * 170)
print("ROTULOS EM CADA SUBTOPICOS: ")
#

# Exibir os rótulos de cada subtópico
for i, rotulo in enumerate(rotulos_gerados):
    print(f"Subtópico {i+1}: {rotulo}")

# for i in subtopicos:
#   print(i)



# print("-" * 170)
# print("RESULTADO DO PROCESSAMENTO DO TEXTO:")
# print(resultado3)
# print()

# print("QUANTIDADE DE SENTENÇAS")
# print(len(resultado3)) # 19
# print("-" * 170)

# print("RESULTADO DO CALCULO DE SIMILARIDADE:")
# print(resultado_similaridade1) # [0.33806170189140655, 0.5714285714285714, 0.3086066999241838, 0.18257418583505536, 0.5477225575051661, 0.4629100498862757, 0.33806170189140655, 0.19999999999999996, 0.5999999999999999, 0.2581988897471611, 0.0, 0.47140452079103173, 0.0, 0.5070925528371099, 0.16903085094570328, 0.0, 0.4472135954999579, 0.19999999999999996]
# print()

# print("QUANTIDADE DE SIMILARIDADES")
# print(len(resultado_similaridade1)) # 18
# print(f"media similiridade {media}") # 0.3112392154546127
# print("-" * 170)

# print("SENTENÇAS:")
# print(frases)
# print("-" * 170)



# print("-" * 170)

# obs: tenho uma lista com as similaridades das sentencas, o que tenho que fazer agora?