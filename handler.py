import json
import boto3
 
def hello(event, context):
    # Captura o nome do bucket: “helloworld-zappts”
    bucket = event['Records'][0]['s3']['bucket']['name']
 
    # Captura o nome da chave do arquivo: “files/arquivo.txt”
    key = event['Records'][0]['s3']['object']['key']
 
    # Instanciando recurso do serviço S3
    s3 = boto3.client("s3")
 
    # Obtém arquivo do Amazon S3
    obj = s3.get_object(Bucket=bucket,Key=key)