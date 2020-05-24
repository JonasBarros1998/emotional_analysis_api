import os
import matplotlib.pyplot as plt
from src.processing_language_natural.dataframe.dataframe import list_dataframe
from src.utils.amazon.s3.saveImagesBucket import SaveFileBucket
from wordcloud import WordCloud
import random

class GearWordCloud():

    def __init__(self):
        self._file_url = ""
        self.word_cloud()
    
    #Definir o nome do arquivo
    def __define_name_file(self):
        aleatory_number = random.randrange(100000)
        file = f"images/word_cloud-{aleatory_number}.jpg"
        return  file

    #Gerar a wordcloud
    def word_cloud(self): 
        file = self.__define_name_file()
        dataframe = list_dataframe()
        dataframe_frequency = dataframe[0]
        #transformando a coluna de um dataframe em um array
        text_array = dataframe_frequency["comments"].array
        #convertendo para um unico texto todos os items do array
        text_join = ' '.join(text_array)
        wordcloud = WordCloud(max_font_size=40, width=600, height=400).generate(text_join)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        save_image = f"{os.path.dirname(__file__)}/{file}"
        wordcloud.to_file(save_image)
        image = {
            "name": file,
            "file": save_image
        }

        self.save_word_cloud(image)
        self.__url_wordcloud(file)

    def save_word_cloud(self, file):
        name_bucket = "appwordcloud"
        self.save_file_bucket = SaveFileBucket()
        self.save_file_bucket.requestImages(name_bucket, file)

    def __url_wordcloud(self, file):
        base_url = "https://appwordcloud.s3-sa-east-1.amazonaws.com"
        file_path = file
        link = f"{base_url}/{file_path}"
        self._file_url = link

    def __str__(self):
        return self._file_url