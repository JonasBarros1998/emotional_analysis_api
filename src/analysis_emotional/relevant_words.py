from nltk import FreqDist, tokenize
from src.processing_language_natural.dataframe.dataframe import list_dataframe

class RelevantWords():
    def __init__(self, total_words = 15):
        self._data = []
        self._total_words = total_words
        self.frequency_word()

    def frequency_word(self):
        list_df = list_dataframe()
        dataframe_frequency = list_df[0]
        word_punct_tokenize = tokenize.WordPunctTokenizer()
        #transformando a coluna de um dataframe em um array
        text_array = dataframe_frequency["comments"].array
        #convertendo para um unico texto todos os items do array
        text_join = ' '.join(text_array)
        #tokenizar o todo o texto
        tokens = word_punct_tokenize.tokenize(text_join)
        #Calculando a frequencia de cada palavra
        freq_dist = FreqDist(tokens)

        count_frequency = list(freq_dist) 
        total_word_frequency = count_frequency[:self._total_words]
        self._data = total_word_frequency

    def __getitem__(self, key):
        return self._data[key]

