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
                                                                # FUNÇÃO ???

#aqui vai separar em blocos e colocar os topicos logo abaixo
def separarSentencasEtopicos(mediaSimilaridades, listaDasSimilaridades, listaEntidades):
  #separar as sentencas
  stop_words = set(stopwords.words('portuguese'))
  sentencasMaiusculas=nltk.tokenize.sent_tokenize(texto)
  listaPalavrasLimpas=[]
  contadorUnicas=0
  contadorUnidas=0
  for i in range(len(listaDasSimilaridades)):
    if listaDasSimilaridades[i]>=mediaSimilaridades: #se a similaridade for acima da media das similaridades entao vai pegar as similaridades de duas sentencas no minimo
      listaTopicos=[]
      contadorUnidas=0
      sentencasSimilaresUnidas="\n" + sentencasMaiusculas[i]+"\n" + sentencasMaiusculas[i+1] + "\n" #aqu vai pegar 2 sentencas e uni-las como antes, refiz o processo pq n sabia
      #como unir com o processo ja feito antes
      print("SENTENCAS COM SIMILARIDADE \n", sentencasSimilaresUnidas)
      sentencasSimilaresUnidas=word_tokenize(sentencasSimilaresUnidas.lower())
      for palavrasUnidas in sentencasSimilaresUnidas:
        if palavrasUnidas.isalnum() and palavrasUnidas not in stop_words:
          listaPalavrasLimpas.append(palavrasUnidas)
      frequencia=FreqDist(listaPalavrasLimpas)
      frequenciaTopicos=frequencia.most_common(5) #aqui sao as palavras mais frequentes da sentencas, pode ser usadas nos topicos, tem a palavra e quantas vezes apareceu
  # print(frequenciaTopicos)
      for topico in frequenciaTopicos:
        if topico[1]>=2:
          listaTopicos.append(topico[0]) #aqui vai na lista de palavras frequentes de antes e pega somente a palavra, sem a quantidade de repeticoes. Ai se caso uma palavra
          #apareceu mais de 2 vezes, bota na lista de topicos
    # print("palavra/palavras com mais de uma aparicao em ambas as frases que estao sendo comparadas", listaTopicos)
    # print(listaPalavrasTopicos1)
      if len(listaTopicos)<5: #tem q ter 5 palavras topicos, entao se tem menos de 5 palavras ainda, vai colocar as entidades pra completar 5 palavras
        contador=0
        if len(listaEntidades[contadorUnidas + contadorUnicas]) > 0:
          while len(listaTopicos) < 5 and contador < len(listaEntidades[contadorUnidas + contadorUnicas]):
            listaTopicos.append(listaEntidades[contadorUnidas+contadorUnicas][contador])
            contador+=1
      if len(listaTopicos)<5: #se caso ainda n completou, vai pegar o resto de palavras da sentenca e vai inserir nos topicos
        for j in range(len(frequenciaTopicos)):
          if frequenciaTopicos[j][0] not in listaTopicos and len(listaTopicos)<5:
            listaTopicos.append(frequenciaTopicos[j][0])
      contadorUnidas+=1
      print("OS 5 TOPICOS \n", listaTopicos, "\n")
    if listaDasSimilaridades[i]<mediaSimilaridades: #aqui é a mesma coisa de antes, so que quando a similaridade for abaixo da media, o q muda de antes acho que é so no
      #primeiro if, talvez da pra unir em um so processo
      listaPalavrasLimpas=[]
      listaTopicos=[]
      sentencasSimilaridade=sentencasMaiusculas[i+contadorUnidas]
      print("SENTENCAS SEM SIMILARIDADE \n", sentencasSimilaridade, "\n")
      # contadorUnicas+=1
      sentencasSimilaridade=word_tokenize(sentencasSimilaridade.lower())
      for palavrasUnidas in sentencasSimilaridade:
        if palavrasUnidas.isalnum() and palavrasUnidas not in stop_words:
          listaPalavrasLimpas.append(palavrasUnidas)
      frequencia=FreqDist(listaPalavrasLimpas)
      frequenciaTopicos=frequencia.most_common(5)
      for topico in frequenciaTopicos:
        if topico[1]>=2:
          listaTopicos.append(topico[0])
      # print("palavra/palavras com mais de uma aparicao em ambas as frases que estao sendo comparadas", listaTopicos)
      # print(listaPalavrasTopicos1)
      if len(listaTopicos)<5:
        contador=0
        if len(listaEntidades[contadorUnidas + contadorUnicas]) > 0:
          while len(listaTopicos) < 5 and contador < len(listaEntidades[contadorUnidas + contadorUnicas]):
            listaTopicos.append(listaEntidades[contadorUnidas + contadorUnicas][contador])
            contador += 1
      if len(listaTopicos)<5:
        for j in range(len(frequenciaTopicos)):
          if frequenciaTopicos[j][0] not in listaTopicos and len(listaTopicos)<5:
            listaTopicos.append(frequenciaTopicos[j][0])
      contadorUnicas+=1
      print("\nOS 5 TOPICOS \n", listaTopicos, "\n")
