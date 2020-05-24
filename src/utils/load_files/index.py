import csv
import json
import requests

#Função para carregar arquivos csv
def check_file_csv():
    with open('file_csv', newline=' ') as csvfile:
        reader = csv.reader(csvfile, delimiter = " ", quotechar='|')
        for row in reader:
            print(row)

def load_file_json(file):
    """
    Função para carregar o arquivo csv, apartir do link enviado pelo usuario

    Parametros: 

    `file`: url do arquivo a ser carregado
    """
    try:
        file_json = requests.get(file)
        status = file_json.status_code
        if(not status == 200):
            return "File not found", status
        return file_json.text, status
    except:
        return "File not found", "404"



