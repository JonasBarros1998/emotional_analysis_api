"""
Arquivo para contar as frequencias de todas as palavras apresentadas no texto. 
Ou seja vai ser devolvivo um dict com as palavras e as frequencas mais utilizadas no texto.
"""

from src.processing_language_natural.dataframe.dataframe import list_dataframe
from nltk import tokenize, FreqDist, WhitespaceTokenizer
import pandas as pd

class HigherFrequencies:
    def __init__(self):
        self.__frequency = {}
        self.count_frequency()
    
    def count_frequency(self):
        self.__comments_dataframe = list_dataframe()
        read_comment_for_ngrams =  self.__comments_dataframe[0]
        white_space_tokenize = WhitespaceTokenizer()

        #deixando todos os comentarios em um unico texto
        comment_ngrams = ' '.join([text for text in read_comment_for_ngrams["comments"]])
        #separaremos todas as palavras
        comments_tokenize = white_space_tokenize.tokenize(comment_ngrams)

        #Calculamos a frequncia do texto
        freq_dist = FreqDist(comments_tokenize)

        df_freq_dist = pd.DataFrame({
            "word": list(freq_dist.keys()),
            "frequency": list(freq_dist.values())
        })

        higher_frequency = df_freq_dist.sort_values(by="frequency", ascending=False).head(n=20)
        higher_frequency_dict = higher_frequency.to_dict(orient='list')
        self.__frequency["words"] = higher_frequency_dict["word"]
        self.__frequency["frequency"] = higher_frequency_dict["frequency"]
        return self.__frequency


    def __getitem__(self, key):
        return self.__frequency[key]
