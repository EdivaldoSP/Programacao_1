import nltk
import spacy

# nltk.download('stopwords')
# nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from math import sqrt

nlp = spacy.load("pt_core_news_sm")

# PARA VER UM CONTEXTO MELHOR, PODE DESCOMENTAR OS PRINT

# |================================================================[ x ]====================================================================|
                                                 # ESPAÇO PARA DOWNLOAD DE PACOTES E EXTRAS

# python -m spacy download pt_core_news_lg
# python -m spacy download pt_core_news_sm

# pip install -U pip setuptools wheel
# pip install -U spacy
# from spacy import displacy

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

# |================================================================[ x ]====================================================================|
                                                    # FUNÇÃO QUE CALCULA A SIMILARIDADE

def formulaCosseno(lista_com_sentencas_separadas):
  lista_das_similaridades = []

  for indice in range(len(lista_com_sentencas_separadas)-1):
    uniao_duas_sentencas = list(set(lista_com_sentencas_separadas[indice] + lista_com_sentencas_separadas[indice+1]))
    
    # print('Essa é a uniao de 2 sentencas, sem repeticao, para ser usada na comparacao e na formula: ', uniaoDuasSentencas)
    # print('Primeira sentenca a ser comparada:', listaComSentencasSeparadas[k])
    # print('Segunda sentenca a ser comparada: ', listaComSentencasSeparadas[k+1])

    # CRIA OS NÚMEROS DE VEZES QUE APARECE UMA PALAVRA DA "uniao_duas_sentencas" NAS SENTENÇAS EM COMPARAÇÃO

    frequencia_palavras_sentenca1 = [0] * len(uniao_duas_sentencas)
    frequencia_palavras_sentenca2 = [0] * len(uniao_duas_sentencas)

    
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

    # nessa variavel tem uma lista de numeros, cada numero representa se apareceu a palavra referente a mesma posicao comparada
    # a uniao das duas frases em comparacao, sem palavras repetidas. Para visualizar pode printar ou ver no slide da prof em um 
    # slide onde ela fala da formula dos cossenos, q ela usa o exemplo a cat and a frog, la tem uma lista de numeros, a ideia 
    # daquela lista é essa daqui. Essa lista serve so para calcular a similaridade
    
    # print('Quantidade de vezes que aparace cada palavra na primeira sentenca, com base a uniao das sentencas: ', aparecimentoPalavrasSentenca1)
    # print('Quantidade de vezes que aparace cada palavra na segunda sentenca, com base a uniao das sentencas: ', aparecimentoPalavrasSentenca2)

    #------------------------------------------------->                                     <-----------------------------------------------|
                                    # COMEÇA A IMPLEMENTAÇÃO DA FÓRMULA DO COSSENO PARA FAZER A COMPARAÇÃO

    # parte de cima da formula
    numerador = 0

    for i in range(len(uniao_duas_sentencas)):
      produto = frequencia_palavras_sentenca1[i] * frequencia_palavras_sentenca2[i]
      numerador += produto
    # print('Parte de cima da formula da similaridade: ', somatorioCossenoParteSuperior)

    # parte de baixo da formula da somatoria
    variavel_a = 0
    variavel_b = 0
 
    for i in range(len(uniao_duas_sentencas)):
      variavel_a += frequencia_palavras_sentenca1[i] ** 2
      variavel_b += frequencia_palavras_sentenca2[i] ** 2

    denominador = sqrt((variavel_a * variavel_b))
    # print('Parte de baixo da formula da similaridade: ', somatorioCossenoParteInferior)

    # calculando somatoria final
    resultado_comparacao = numerador / denominador

    # print('Esse é o resultado da formula entre as 2 sentencas acima:', resultadocomparacao)
    
    # criando uma lista com o resultado de todas as somatorias finais
    # tipo: comparacao sent0 com sent1, sent1 com sent2, sent2 com sent3, etc.

    lista_das_similaridades.append(resultado_comparacao)
    
  return lista_das_similaridades

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

# |================================================================[ x ]====================================================================|
                                                              # FUNÇÃO ???

# nesse def vai criar uma lista, com mini listas dentro. Cada mini lista vai ter algumas palavras que sao as entidades de cada bloco de sentenca (bloco de sentenca seria
# as sentencas juntas quando similares ou sozinhas se nao similares, cada bloco vai ter uma lista de palavras de entidades), as entidades sao tipo nomes, lugares, eventos etc.,
# basicamente palavras chaves que podem ser usadas como palavras nos topicos, elas sao achadas com o spacy

def spacysentencas(lista_das_similaridades):
  lista_entidades = []

  for i in range(len(lista_das_similaridades)): 
    # vai executar o negocio a quantidade de blocos, entao tipo em um texto de 4 sentencas, e a sentenca 1 ta junta com sentenca 2
    # por causa de similaridade ja vai ser um bloco, e a sentenca 3 e 4 tao sozinhas pq tem similaridade com nd, entao sao 3 blocos (sent1+sent2, sent3, sent4), entao o for ai
    # vai ser feito 3 vezes, para achar as entidades de 3 sentencas, nesse exemplo.

    contador_unidas = 0

    if lista_das_similaridades[i] != 0: # aqui se a similaridade for diferente q 0, significa que tem similaridade, logo sao pelo menos 2 sentencas juntas
      frase = nltk.tokenize.sent_tokenize(texto)
      sentenca1 = nlp(str(frase[i+contador_unidas]))
      sentenca2 = nlp(str(frase[i+1+contador_unidas])) 
      # o i+1 é pq a sentenca i é uma sentenca, e quero pegar logo a proxima, entao i+1

      print("primeira frase para buscar as entidades com spacy: ", sentenca1)
      print("segunda frase para buscar as entidades com spacy: ", sentenca2)

      lista_entidades1 = [] # vai receber as entidades da sentenca 1
      lista_entidades2 = [] # vai receber as entidades da sentenca 2

      lista_palavras_topicos1 = []

      for entidades_da_sentenca1 in sentenca1.ents:
        print(f"a frase - {sentenca1} - tem entidade: " , lista_entidades1, "|", entidades_da_sentenca1.label_)
        lista_entidades1.append(entidades_da_sentenca1.label_)
        lista_palavras_topicos1.append(entidades_da_sentenca1)

      for entidades_da_sentenca2 in sentenca2.ents:
        print(f"a frase - {sentenca2} - tem entidade: " , lista_entidades2, "|", entidades_da_sentenca2.label_)
        lista_entidades2.append(entidades_da_sentenca2.label_)
        lista_palavras_topicos1.append(entidades_da_sentenca2)

      lista_entidades.append(lista_palavras_topicos1)

      print("LISTA PALAVRAS TOPICOS 1", lista_palavras_topicos1)
      
      # print("reconhecimento de entidades frase 1", lista_entidades1)   
      # print("reconhecimento de entidades frase 2", lista_entidades2)
    
    contador_unidas += 1

    if lista_das_similaridades[i] == 0: # aqui a similaridade de uma sentenca é 0, entao ela vai ser um bloco de uma unica sentenca
        frase = nltk.tokenize.sent_tokenize(texto)
        sentenca1 = nlp(str(frase[i+contador_unidas])) 
        # o frase[i] é pq quero pegar a sentenca q ta indicada pela ordem do primeiro for la no topo+contadorUnidas pq se caso
        # ja teve uma comparacao anterior, vai ser pego a proxima sentenca, senao pega a mesma sentenca que foi pega antes

        # print("\nprimeira frase para buscar as entidades com spacy ", sentenca1)

        listaEntidades1 = []
        listaPalavrasTopicos1 = []

        for entidadesDaSentenca1 in sentenca1.ents:
          # print(f"a frase - {sentenca1} - tem entidade: " , entidadesDaSentenca1, "|", entidadesDaSentenca1.label_)
          listaEntidades1.append(entidadesDaSentenca1.label_)
          listaPalavrasTopicos1.append(entidadesDaSentenca1)

        lista_entidades.append(listaPalavrasTopicos1)

        # print("reconhecimento de entidades frase 1", listaEntidades1)
        # print(listaPalavrasTopicos1)
        # print("LISTA PALAVRAS TOPICOS 1", listaPalavrasTopicos1)

  # print(listaEntidades) #essa lista é a mesma coisa da primeira lista de sentencas, com mini listas, so que ai é com as entidades
  return lista_entidades

# |================================================================[ x ]====================================================================|
                                                                # FUNÇÃO ???

# aqui vai separar em blocos e colocar os topicos logo abaixo

def separarSentencasEtopicos(mediaSimilaridades, listaDasSimilaridades, listaEntidades):
  #separar as sentencas
  stop_words = set(stopwords.words('portuguese'))
  sentencasMaiusculas = nltk.tokenize.sent_tokenize(texto)
  listaPalavrasLimpas = []
  contadorUnicas = 0
  contadorUnidas = 0

  for i in range(len(listaDasSimilaridades)):
    if listaDasSimilaridades[i] >= mediaSimilaridades: # se a similaridade for acima da media das similaridades entao vai pegar as similaridades de duas sentencas no minimo
      listaTopicos =[ ]
      contadorUnidas = 0
      sentencasSimilaresUnidas = "\n" + sentencasMaiusculas[i] + "\n" + sentencasMaiusculas[i+1] + "\n" #aqu vai pegar 2 sentencas e uni-las como antes, refiz o processo pq n sabia
      # como unir com o processo ja feito antes
      #print("SENTENCAS COM SIMILARIDADE \n", sentencasSimilaresUnidas)
      sentencasSimilaresUnidas = word_tokenize(sentencasSimilaresUnidas.lower())
      for palavrasUnidas in sentencasSimilaresUnidas:
        if palavrasUnidas.isalnum() and palavrasUnidas not in stop_words:
          listaPalavrasLimpas.append(palavrasUnidas)

      frequencia = FreqDist(listaPalavrasLimpas)
      frequenciaTopicos = frequencia.most_common(5) #aqui sao as palavras mais frequentes da sentencas, pode ser usadas nos topicos, tem a palavra e quantas vezes apareceu
  
  # print(frequenciaTopicos)

      for topico in frequenciaTopicos:
        if topico[1] >= 2:
          listaTopicos.append(topico[0]) 
          # aqui vai na lista de palavras frequentes de antes e pega somente a palavra, sem a quantidade de repeticoes. Ai se caso uma palavra
          # apareceu mais de 2 vezes, bota na lista de topicos

    # print("palavra/palavras com mais de uma aparicao em ambas as frases que estao sendo comparadas", listaTopicos)
    # print(listaPalavrasTopicos1)

      if len(listaTopicos) < 5: # tem q ter 5 palavras topicos, entao se tem menos de 5 palavras ainda, vai colocar as entidades pra completar 5 palavras
        contador = 0

        if len(listaEntidades[contadorUnidas + contadorUnicas]) > 0:
          while len(listaTopicos) < 5 and contador < len(listaEntidades[contadorUnidas + contadorUnicas]):
            listaTopicos.append(listaEntidades[contadorUnidas + contadorUnicas][contador])
            contador += 1

      if len(listaTopicos) < 5: # se caso ainda n completou, vai pegar o resto de palavras da sentenca e vai inserir nos topicos
        for j in range(len(frequenciaTopicos)):
          if frequenciaTopicos[j][0] not in listaTopicos and len(listaTopicos) < 5:
            listaTopicos.append(frequenciaTopicos[j][0])

      contadorUnidas += 1

      #print("OS 5 TOPICOS \n", listaTopicos, "\n")

    if listaDasSimilaridades[i] < mediaSimilaridades: 
      # aqui é a mesma coisa de antes, so que quando a similaridade for abaixo da media, o q muda de antes acho que é so no
      # primeiro if, talvez da pra unir em um so processo

      listaPalavrasLimpas = []
      listaTopicos = []

      sentencasSimilaridade = sentencasMaiusculas[i+contadorUnidas]
      #print("SENTENCAS SEM SIMILARIDADE \n", sentencasSimilaridade, "\n")

      sentencasSimilaridade = word_tokenize(sentencasSimilaridade.lower())

      for palavrasUnidas in sentencasSimilaridade:
        if palavrasUnidas.isalnum() and palavrasUnidas not in stop_words:
          listaPalavrasLimpas.append(palavrasUnidas)

      frequencia = FreqDist(listaPalavrasLimpas)
      frequenciaTopicos = frequencia.most_common(5)

      for topico in frequenciaTopicos:
        if topico[1] >= 2:
          listaTopicos.append(topico[0])

      # print("palavra/palavras com mais de uma aparicao em ambas as frases que estao sendo comparadas", listaTopicos)
      # print(listaPalavrasTopicos1)

      if len(listaTopicos) < 5:
        contador = 0

        if len(listaEntidades[contadorUnidas + contadorUnicas]) > 0:
          while len(listaTopicos) < 5 and contador < len(listaEntidades[contadorUnidas + contadorUnicas]):
            listaTopicos.append(listaEntidades[contadorUnidas + contadorUnicas][contador])
            contador += 1

      if len(listaTopicos)<5:
        for j in range(len(frequenciaTopicos)):
          if frequenciaTopicos[j][0] not in listaTopicos and len(listaTopicos)<5:
            listaTopicos.append(frequenciaTopicos[j][0])

      contadorUnicas += 1
      #print("\nOS 5 TOPICOS \n", listaTopicos, "\n")

# |================================================================[ x ]====================================================================|

#print()

#texto = 'A ginasta Jade Barbosa, que obteve três medalhas nos Jogos Pan-Americanos do Rio, em julho, venceu votação na internet e será a representante brasileira no revezamento da tocha olímpica para Pequim-2008. A tocha passará por vinte países, mas o Brasil não estará no percurso olímpico. Por isso, Jade participará do evento em Buenos Aires, na Argentina, única cidade da América do Sul a receber o símbolo dos Jogos. O revezamento terminará em 8 de agosto, primeiro dia das Olimpíadas de Pequim.'
texto = 'Os artistas brasileiros têm tido reconhecimento mundial. Dentre os artistas, destacam-se Anitta, Caetano Veloso e Gilberto Gil. Todos eles já ganharam notórias premiações.'

lista = listaTokenizada(texto)
cosseno = formulaCosseno(lista)
media = mediaSentencas(cosseno)
spcy = spacysentencas(cosseno)
separar = separarSentencasEtopicos(media, cosseno, spcy)

# print(spcy)

#print()
# print('Todos os resultados que foram gerados por meio da formula das somatorias. Depois é a média entre elas): ', cosseno, media)

#falta:

# botar os numeros ate 2 casas decimais
# ver se a separacao em def ta ok
# perguntar se pode def sem return
# ver as aspas para python mais antigos

# limitacoes:

# o codigo ta meio limitado em 2 sentencas em cada bloco onde sentencas tem similaridades, se caso tiver um bloco com 3 sentencas unidas similares ou mais, acho q n funciona
# as palavras nos topicos, quando tem poucas palavras repetidas mais de 2 vezes e poucas entidades, acabam entrando as primeiras palavras da sentenca, mesmo n sendo
# palavras importantes

# with open ("Riccardo_colab/texto_auxiliar.txt") as arquivo:
#   programacao = arquivo.read()
#   print(programacao)
# print("-" * 170)
# # texto3 = "Os artistas brasileiros têm tido reconhecimento mundial. Dentre os artistas, destacam-se Anitta, Caetano Veloso e Gilberto Gil. Todos eles já ganharam notórias premiações."

# saida3 = listaTokenizada(programacao)
# print(saida3)
# print("-" * 170)
# resultado = formulaCosseno(saida3)
# print(resultado)
# print("-" * 170)