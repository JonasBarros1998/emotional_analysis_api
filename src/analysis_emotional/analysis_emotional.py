from nltk import tokenize, FreqDist
from wordcloud import WordCloud
from src.utils.load_files.index import load_file_json
from src.processing_language_natural.dataframe.dataframe import read_database
from src.processing_language_natural.text_processing.processing import main
from src.analysis_emotional.wordcloud import GearWordCloud
from src.analysis_emotional.relevant_words import RelevantWords
from src.analysis_emotional.higher_frequencies import HigherFrequencies
from src.analysis_emotional.ngrams import Ngrams

class EmotionalAnalisys:

    def __init__(self, url, total_words = 15):
        self._datas = {}
        self.__loading_file(url)
        self.frequency_word()
        self.word_cloud()
        self.words_frequencies()
        self.ngrams()

    def __loading_file(self, url):
        file, status = load_file_json(url)
        if  (not status == 200):
            return file
        #Faço a criação de um dataframe
        read_database(file)
        #Função para fazer o processamento dos comentarios
        main()
    
    #Metodo para exportas as palavras mais relevantes
    def frequency_word(self):
        relevant_words = RelevantWords()
        self._datas["relevant_words"] = relevant_words[:]
        
    #Metodo para gerar a wordcloud
    def word_cloud(self):
        gear_word_cloud = GearWordCloud()
        self._datas["link_wordcloud"] = str(gear_word_cloud)
    
    def words_frequencies(self):
        higher_frequencies  = HigherFrequencies()
        self._datas["higher_frequencies"] = {
            "words": higher_frequencies["words"], 
            "frequency": higher_frequencies["frequency"]
        }
    
    def ngrams(self):
        ngrams = Ngrams()
        self._datas["ngrams"] = ngrams[:]

    def __getitem__(self, key):
        return self._datas
