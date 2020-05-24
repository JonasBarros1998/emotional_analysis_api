from nltk import tokenize, FreqDist, WhitespaceTokenizer, ngrams
from sklearn.feature_extraction.text import TfidfVectorizer
from src.processing_language_natural.dataframe.dataframe import list_dataframe
import pandas as pd

class Ngrams:
    def __init__(self):
        self.__ngrams = []
        self.processing_ngrams()

    #Processamento de texto com Ngrams
    def processing_ngrams(self):
        self.__comments_dataframe = list_dataframe()
        read_comment_for_ngrams =  self.__comments_dataframe[0]
        white_space_tokenize = WhitespaceTokenizer()

        #deixando todos os comentarios em um unico texto
        #comment_ngrams = ' '.join([text for text in read_comment_for_ngrams["comments"]])
        #separaremos todas as palavras
        #comments_tokenize = white_space_tokenize.tokenize(comment_ngrams)

        #Guardamos na variavel frequencia de cada palavra no texto
        #freq_dist = FreqDist(comments_tokenize)

        #df_freq_dist = pd.DataFrame({
        #    "word": list(freq_dist.keys()),
        #    "frequency": list(freq_dist.values())
        #})

        #Verificando a frequencia com um par de palavras
        #gear_ngrams = ngrams(freq_dist.keys(), 2)
        #print(list(gear_ngrams))
        corpus = read_comment_for_ngrams["comments"]
        tfidf_vactorize = TfidfVectorizer(ngram_range=(2, 2))
        tfidf_vactorize.fit_transform(corpus)
        names_ngrams = tfidf_vactorize.get_feature_names()
        self.__ngrams = names_ngrams

        #order = df_freq_dist.nlargest(columns="frequency", n=15)
        #self.__ngrams.append()
    
    def __getitem__(self, key):
        return self.__ngrams[key]