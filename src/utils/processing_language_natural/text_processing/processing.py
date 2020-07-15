"""
Arquivo para fazer o  tratamento geral do texto. 

Esses tratamentos são: 
standardize_text: normalizar o texto(padronizar todas as letras).
stop_words: Retirar do texto todas as plavaras que não vão mudar o sentido da frase. 
caracteres_specials: Retirar todos os caracteres especiais presentes do texto. 
"""

import nltk
import pandas as pd
from nltk import tokenize
import unidecode
from string import punctuation
from src.processing_language_natural.dataframe.dataframe import list_dataframe, update_dataframe
from nltk import tokenize, FreqDist, WhitespaceTokenizer, ngrams

comments_dataframe =  list_dataframe()

def main():
    #função para formatar todos os comentarios para minusculos
    standardize_text()
    #função para retirar as stopwords do texto
    delete_stop_words()
    #Função para retirar pontuação e caracteres especiais do texto
    caracteres_specials()


# Padronização do texto
# - Todas as letras do texto minusculas
def standardize_text():
    comments_db = comments_dataframe[0]
    #Retirando os acentos das palavras
    comment = [unidecode.unidecode(comment) for comment in comments_db['comments']]
    comments_db['comments'] = comment
    #normalizando todas as palavras
    commnt_lowercase = [comment.lower() for comment in comments_db['comments']]
    comments_db['comments'] = commnt_lowercase
    update_dataframe(comments_db)

#**Tratamento de caracteres especiais**
#1. Excluindo o stop words do texto
def delete_stop_words():
    comments_db_for_stopwords = comments_dataframe[0]
    nltk.download('stopwords')
    stop_words = nltk.corpus.stopwords.words("portuguese")

    pharase_without_stop_words = []
    for comment in comments_db_for_stopwords['comments']:
        new_comment = []
        comment_split = comment.split()
        for words in comment_split:
            if(words not in stop_words):
                new_comment.append(words)
    
        pharase_without_stop_words.append(' '.join(new_comment))

    comments_db_for_stopwords['comments'] = pharase_without_stop_words
    update_dataframe(comments_db_for_stopwords)

#2. Excluindo pontuação e os caracteres especiais do texto
def caracteres_specials():
    comments_db_for_carac_specials = comments_dataframe[0]
    punct = punctuation + "…"
    token = tokenize.WordPunctTokenizer()

    comment_whitout_punctuation = []
    for comment in comments_db_for_carac_specials['comments']:
        comments = []
        separate_comment = token.tokenize(comment)
        for word in separate_comment:
            if(word not in punct):
                comments.append(word)     
  
        comment_whitout_punctuation.append(' '.join(comments))

    comments_db_for_carac_specials['comments'] = comment_whitout_punctuation
    update_dataframe(comments_db_for_carac_specials)
