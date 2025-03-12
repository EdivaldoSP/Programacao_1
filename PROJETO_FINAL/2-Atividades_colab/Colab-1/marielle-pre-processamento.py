import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# nltk.download('punkt_tab') # Usado na tokenização
# nltk.download('stopwords') # Módulo para stopwords
# nltk.download('rslp') # Módulo para radicalizar
# nltk.download('averaged_perceptron_tagger_eng')

# FAZENDO A LEITURA DO ARQUIVO .TXT

with open ("Colab-2/mariele.txt", "r", encoding="UTF-8") as arquivo:
    texto = arquivo.read()
    #print(texto)

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

resultado = pre_processamento(texto)

for i in resultado:
    print(i)