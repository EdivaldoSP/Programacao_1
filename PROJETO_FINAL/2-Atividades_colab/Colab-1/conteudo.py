import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# nltk.download('punkt_tab') # Usado na tokenização
# nltk.download('stopwords') # Módulo para stopwords
# nltk.download('rslp') # Módulo para radicalizar
# nltk.download('averaged_perceptron_tagger_eng')

# |=============================================[ x ]=================================================|
                                    # APLICAÇÃO DE TOKENIZAÇÃO

texto1 = "Quando o mistério é grande demais, a gente não ousa desobedecer."
tokens1 = word_tokenize(texto1)

#print(tokens1) #-----> # observe que o resultado é uma lista contendo tokens.

# |=============================================[ x ]=================================================|
texto2 = "Python é uma boa linguagem de programação. PLN é um terreno cheio de buracos."
tokens2 = word_tokenize(texto2)

# print(tokens2) #-----> # observe que o resultado é uma lista contendo tokens.

# |=============================================[ x ]=================================================|
                                    # TOKENIZANDO POR SENTENÇAS

sentencas = nltk.tokenize.sent_tokenize(texto2)

#print(sentencas)  # -----> # observe que o resultado é uma lista contendo as sentenças

# |=============================================[ x ]=================================================|
                    # NORMALIZANDO AS SENTENÇAS USANDO A FUNCÃO LOWER NATIVA DO PYTHON

# obs: normalizar significa transformar todas as letras das palavras em minúsculas ou maiúsculas.

sentencas_normalizadas = []

for palavra in sentencas:
    minusculas = palavra.lower()
    sentencas_normalizadas.append(minusculas)

# print(sentencas_normalizadas)

# |=============================================[ x ]=================================================|
                                        # LIST COMPREHENSION

# Podemos ter o mesmo reusltado da seguinte forma

sentencas_normalizadas = [palavra.lower() for palavra in sentencas]
#print(sentencas_normalizadas)

# |=============================================[ x ]=================================================|
                                            # STOPWORDS

# São palavras que, em sua maioria, são muito frequentes e não agregam valor substancial na tarefa de 
# análise, como "de", "a", "o", "em", "para", "com", entre outras.

stopwords = nltk.corpus.stopwords.words("portuguese")

# |=============================================[ x ]=================================================|
                                        # REMOVENDO STOPWORDS
                                        
sentencas_limpas = [] # --> setenças sem as stopswords e em lowercase

for sentenca in sentencas_normalizadas:
    tokens = word_tokenize(sentenca)

    token_limpo = []
    for palavra in tokens:
        if palavra not in stopwords and palavra.isalnum():
            token_limpo.append(palavra)
    sentencas_limpas.append(token_limpo)

#print(sentencas_limpas)

# |=============================================[ x ]=================================================|