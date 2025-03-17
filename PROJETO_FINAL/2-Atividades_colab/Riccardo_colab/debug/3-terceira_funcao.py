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
                                              # FUNÇÃO QUE CALCULA A MÉDIA ENTRE AS SENTENÇAS

def mediaSentencas(lista_das_similaridades):
  # achar a media entre as similaridades

  soma_similaridades = 0
  quantidade_similaridades = len(lista_das_similaridades)

  for similaridade_entre_sentencas in lista_das_similaridades:
    soma_similaridades += similaridade_entre_sentencas
    #quantidade_de_similaridades += 1

  media_similaridades = soma_similaridades / quantidade_similaridades

  return media_similaridades
