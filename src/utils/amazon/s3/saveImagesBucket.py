"""
Modulo serve apenas para enviar arquivos(podendo ser de
qualquer tipo), para o bucket do s3.
"""
import io
import os
import boto3
from botocore.client import ClientError
from abc import ABC, abstractmethod
import logging
from PIL import Image 


class SaveFileBucket():
    def __init__(self):
        self.__s3Client = boto3.client('s3',
        aws_access_key_id = os.getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key = os.getenv("AWS_SECRET_KEY")
        )

    def requestImages(self, bucket, files):
        '''
        `bucket`: Nome do bucket

        `files`: Dict com a imagem a ser salva no s3

        Exemplo de como o dict deverá ficar: 

        { 
            name: nome da imagem, o nome da imagem não pode conter a extensão.
            
            file: Localização da imagem ou o buffer(caso a imgem ser enviada apartir de um request)      
        '''

        image = Image.open(files['file'])
        byte_image = io.BytesIO()
        image.save(byte_image, "JPEG")
        byte_image.seek(0)
        self.__saveImages(byte_image, files["name"], bucket)

    def __saveImages(self, body, key, bucket):

        try:
            self.__s3Client.put_object(ACL='public-read',
                                                    Body=body,
                                                    Key=key,
                                                    Bucket=bucket)
            logging.info("A imagem foi salva")

        except ClientError as error:
            logging.error(error)
            return {"status": str(error)}