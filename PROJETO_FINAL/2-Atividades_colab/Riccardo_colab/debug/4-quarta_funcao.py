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

# nesse def vai criar uma lista, com mini listas dentro. Cada mini lista vai ter algumas palavras que sao as entidades de cada bloco de sentenca (bloco de sentenca seria
# as sentencas juntas quando similares ou sozinhas se nao similares, cada bloco vai ter uma lista de palavras de entidades), as entidades sao tipo nomes, lugares, eventos etc.,
# basicamente palavras chaves que podem ser usadas como palavras nos topicos, elas sao achadas como o spacy

def spacysentencas(lista_das_similaridades):
  listaEntidades = []
  for i in range(len(lista_das_similaridades)): 
    #vai executar o negocio a quantidade de blocos, entao tipo em um texto de 4 sentencas, e a sentenca 1 ta junta com sentenca 2
    #por causa de similaridade ja vai ser um bloco, e a sentenca 3 e 4 tao sozinhas pq tem similaridade com nd, entao sao 3 blocos (sent1+sent2, sent3, sent4), entao o for ai
    #vai ser feito 3 vezes, para achar as entidades de 3 sentencas, nesse exemplo
    contador = 0
    contadorUnidas = 0

    if lista_das_similaridades[i]!=  0: #aqui se a similaridade for diferente q 0, significa que tem similaridade, logo sao pelo menos 2 sentencas juntas
      frase = nltk.tokenize.sent_tokenize(texto)
      sentenca1 = nlp(str(frase[i+contadorUnidas]))
      sentenca2 = nlp(str(frase[i+1+contadorUnidas])) #o i+1 é pq a sentenca i é uma sentenca, e quero pegar logo a proxima, entao i+1

      # print("\nprimeira frase para buscar as entidades com spacy ", sentenca1)
      # print("segunda frase para buscar as entidades com spacy ", sentenca2)

      listaEntidades1 = [] #vai receber as sentencas da sentenca 1
      listaEntidades2 = [] #aqui da segunda
      listaPalavrasTopicos1 = []

      for entidadesDaSentenca1 in sentenca1.ents:
        # print(f"a frase - {sentenca1} - tem entidade: " , entidadesDaSentenca1, "|", entidadesDaSentenca1.label_)
        listaEntidades1.append(entidadesDaSentenca1.label_)
        listaPalavrasTopicos1.append(entidadesDaSentenca1)

      for entidadesDaSentenca2 in sentenca2.ents:
        # print(f"a frase - {sentenca2} - tem entidade: " , entidadesDaSentenca2, "|", entidadesDaSentenca2.label_)
        listaEntidades2.append(entidadesDaSentenca2.label_)
        listaPalavrasTopicos1.append(entidadesDaSentenca2)

      listaEntidades.append(listaPalavrasTopicos1)

      # print("LISTA PALAVRAS TOPICOS 1", listaPalavrasTopicos1)
      # print("reconhecimento de entidades frase 1", listaEntidades1)
      # print("reconhecimento de entidades frase 2", listaEntidades2)
      # print(listaPalavrasTopicos1)
      # for entidade1 in listaEntidades1:
      #   for entidade2 in listaEntidades2:
      #     if entidade1==entidade2:
      #       contador+=1 #aqui é so um contador de similaridades das entidades, n serve pra nd, pode ignorar
      # print("contador similaridades de entidades, ver quantas vezes tem o mesmo tipo de entidades em ambas as frases", contador)

    contadorUnidas += 1
    if lista_das_similaridades[i] == 0: #aqui a similaridade de uma sentenca é 0, entao ela vai ser um bloco de uma unica sentenca
        frase = nltk.tokenize.sent_tokenize(texto)
        sentenca1 = nlp(str(frase[i+contadorUnidas])) 
        #o frase[i] é pq quero pegar a sentenca q ta indicada pela ordem do primeiro for la no topo+contadorUnidas pq se caso
        #ja teve uma comparacao anterior, vai ser pego a proxima sentenca, senao pega a mesma sentenca que foi pega antes
        # print("\nprimeira frase para buscar as entidades com spacy ", sentenca1)

        listaEntidades1 = []
        listaPalavrasTopicos1 = []
        for entidadesDaSentenca1 in sentenca1.ents:
          # print(f"a frase - {sentenca1} - tem entidade: " , entidadesDaSentenca1, "|", entidadesDaSentenca1.label_)
          listaEntidades1.append(entidadesDaSentenca1.label_)
          listaPalavrasTopicos1.append(entidadesDaSentenca1)

        listaEntidades.append(listaPalavrasTopicos1)

        # print("reconhecimento de entidades frase 1", listaEntidades1)
        # print(listaPalavrasTopicos1)
        # print("LISTA PALAVRAS TOPICOS 1", listaPalavrasTopicos1)

  # print(listaEntidades) #essa lista é a mesma coisa da primeira lista de sentencas, com mini listas, so que ai é com as entidades
  return listaEntidades