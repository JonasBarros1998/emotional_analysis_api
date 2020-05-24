import pandas as pd

dataframe_series = []

def read_database(file):
    """
    Função para fazer a leitura do dataframe apartir de uma ulr, e retornar um dataframe criado pelo pandas

    `file`: recebe uma estrutura de dados json
    """
    read_file = pd.read_json(file)
    dataframe = create_dataframe(read_file)
    return dataframe

def create_dataframe(comments):
    """
    Função usada para criar um dataframe ou series

    `comments`: Recebe um json
    """
    count_comments_db = len(comments) 

    #gerando um Id unico para cada linha do dataframe
    _id = range(0, count_comments_db)

    #Adicionando em uma lista de Id
    define_id = list(_id)

    datas = {
        "_id": define_id, 
        "comments": comments["comment"]
    }

    #Criando o dataframe
    comments_db = pd.DataFrame(data = datas, columns=["_id", "comments"])
    #chamando a função para atualizar o dataframe
    update_dataframe(comments_db)
    return comments_db

def update_dataframe(df_or_series):
    """
    Função para atualizar o dataframe, e retornar o dataframe atualizado

    `df_or_series`: recebe um dataframe ou series do pandas
    """
    
    if(not len(dataframe_series) == 0):
        dataframe_series.pop(0)
        dataframe_series.append(df_or_series)
        return dataframe_series
    
    dataframe_series.append(df_or_series)
    return dataframe_series

def list_dataframe():
    """
        Função usada para fazer a leitura do dataframe ou series
    """
    return dataframe_series