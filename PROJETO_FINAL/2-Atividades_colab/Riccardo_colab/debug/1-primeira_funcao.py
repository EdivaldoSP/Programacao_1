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
                                                # FUNÇAO QUE CRIA UMA LISTA COM DENTRO AS SENTENCAS

def listaTokenizada(texto):
  # NORMALIZANDO O TEXTO (DEIXANDO EM MINÚSCULO)
  texto_minusculas = texto.lower()

  # CRIANDO SENTENCAS COM TOKENS
  sentencas = nltk.tokenize.sent_tokenize(texto_minusculas)
  
  # STOPWORDS
  stop_words = set(stopwords.words('portuguese'))

  # ELIMINANDO STOPWORDS, CARACTERES ESPECIAS, NUMEROS, PONTUAÇÕES, ETC
  lista_com_sentencas_separadas = []
  for sentenca in sentencas:
    tokens = word_tokenize(sentenca)

    token_limpo = []
    for palavra in tokens:
      if palavra not in stop_words and palavra.isalpha():
        token_limpo.append(palavra)
    lista_com_sentencas_separadas.append(token_limpo)

  return lista_com_sentencas_separadas

  # stop_words = set(stopwords.words('portuguese'))
  # listaComSentencasSeparadas=[]
  # textoMinusculas=texto.lower()
  # sentencas=nltk.tokenize.sent_tokenize(textoMinusculas)

  # for sentencaUnica in sentencas:
  #   palavras=word_tokenize(sentencaUnica)
  #   miniListas=[]
  #   for palavraUnica in palavras:
  #     if palavraUnica not in stop_words and palavraUnica.isalpha():
  #       miniListas.append(palavraUnica)
  #   listaComSentencasSeparadas.append(miniListas)

  # print('Essa é a lista com todas as sentencas dentro separadas em uma lista interna cada uma:', listaComSentencasSeparadas)  #agora tem uma lista maior com varias listas dentro, cada uma das mini listas tem uma sentenca (em teoria)
  #return listaComSentencasSeparadas
