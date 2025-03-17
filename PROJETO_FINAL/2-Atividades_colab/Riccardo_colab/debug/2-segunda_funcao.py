import nltk
import spacy

nltk.download('stopwords')
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from math import sqrt

nlp = spacy.load("pt_core_news_lg")

# |================================================================[ x ]====================================================================|
                                                    # FUNÇÃO QUE CALCULA A SIMILARIDADE

def formulaCosseno(lista_com_sentencas_separadas):
  for indice in range(len(lista_com_sentencas_separadas)-1):
    uniao_duas_sentencas = list(set(lista_com_sentencas_separadas[indice] + lista_com_sentencas_separadas[indice+1]))
    
    # print('Essa é a uniao de 2 sentencas, sem repeticao, para ser usada na comparacao e na formula: ', uniaoDuasSentencas)
    # print('Primeira sentenca a ser comparada:', listaComSentencasSeparadas[k])
    # print('Segunda sentenca a ser comparada: ', listaComSentencasSeparadas[k+1])

    # CRIA OS NÚMEROS DE VEZES QUE APARECE UMA PALAVRA DA "uniao_duas_sentencas" NAS SENTENÇAS EM COMPARAÇÃO

    frequencia_palavras_sentenca1 = [0] * len(uniao_duas_sentencas)
    frequencia_palavras_sentenca2 = [0] * len(uniao_duas_sentencas)

    # nessa variavel tem uma lista de numeros, cada numero representa se apareceu a palavra referente a mesma posicao comparada
    # a uniao das duas frases em comparacao, sem palavras repetidas. Para visualizar pode printar ou ver no slide da prof em um 
    # slide onde ela fala da formula dos cossenos, q ela usa o exemplo a cat and a frog, la tem uma lista de numeros, a ideia 
    # daquela lista é essa daqui. Essa lista serve so para calcular a similaridade

    
    # ADICIONANDO A FREQUENCIA DAS PALAVRAS NOS VETORES
    for token in lista_com_sentencas_separadas[indice]:
      frequencia_palavras_sentenca1[uniao_duas_sentencas.index(token)] += 1 
    
    for token in lista_com_sentencas_separadas[indice+1]:
      frequencia_palavras_sentenca2[uniao_duas_sentencas.index(token)] += 1

    # Estamos acessando cada token em "lista_com_sentencas_separadas" percorrendo com o for. 
    # Na primeira repetição, o valor do token é 0, então ele irá acessar o primeiro token (ex: "lorem") em "lista_com_sentencas_separadas[k]".
    # Depois que ele acessar o token "lorem", ele irá verificar em qual posição esse token ocupa na lista "uniao_duas_sentencas"
    # "lorem" ocupa a posição 2 (supondo) em "uniao_duas_sentencas", dessa forma, será acrescentado 1 na mesma posição em "frequencia_palavras_sentenca1" de zeros. 


    # for i in range(len(uniao_duas_sentencas)):
    #   cont = 0
    #   for j in range(len(lista_com_sentencas_separadas[k])):
    #     if uniao_duas_sentencas[i] == lista_com_sentencas_separadas[k][j]:
    #       cont += 1
    #   frequencia_palavras_sentenca1.append(cont) 

    # for i in range(len(uniao_duas_sentencas)):
    #   cont = 0
    #   for j in range(len(lista_com_sentencas_separadas[k+1])):
    #     if uniao_duas_sentencas[i] == lista_com_sentencas_separadas[k+1][j]:
    #       cont += 1
    #   frequencia_palavras_sentenca2.append(cont) #aqui tb é aquela lista com aqueles numeros q tem um exemplo no slide
    
    # print('Quantidade de vezes que aparace cada palavra na primeira sentenca, com base a uniao das sentencas: ', aparecimentoPalavrasSentenca1)
    # print('Quantidade de vezes que aparace cada palavra na segunda sentenca, com base a uniao das sentencas: ', aparecimentoPalavrasSentenca2)

    #------------------------------------------------->                                     <-----------------------------------------------|
                                    # COMEÇA A IMPLEMENTAÇÃO DA FÓRMULA DO COSSENO PARA FAZER A COMPARAÇÃO

  #parte de cima da formula
    numerador = 0

    for i in range(len(uniao_duas_sentencas)):
      produto = frequencia_palavras_sentenca1[i] * frequencia_palavras_sentenca2[i]
      numerador += produto
    # print('Parte de cima da formula da similaridade: ', somatorioCossenoParteSuperior)

    #parte de baixo da formula da somatoria
    variavel_a = 0
    variavel_b = 0
 
    for i in range(len(uniao_duas_sentencas)):
      variavel_a += frequencia_palavras_sentenca1[i] ** 2
      variavel_b += frequencia_palavras_sentenca2[i] ** 2

    denominador = sqrt((variavel_a * variavel_b))
    # print('Parte de baixo da formula da similaridade: ', somatorioCossenoParteInferior)

    #calculando somatoria final
    resultado_comparacao = numerador / denominador

    # print('Esse é o resultado da formula entre as 2 sentencas acima:', resultadocomparacao)
    
    # criando uma lista com o resultado de todas as somatorias finais
    # tipo: comparacao sent0 com sent1, sent1 com sent2, sent2 com sent3, etc.

    lista_das_similaridades = []

    lista_das_similaridades.append(resultado_comparacao)
    
  return lista_das_similaridades
