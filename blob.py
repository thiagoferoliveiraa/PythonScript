import os
import pandas as pd
from azure.storage.blob import BlobServiceClient


# Define as informações de conexão
connection_string = 'Adicionar sua connectin string'

# Inicializa o cliente de serviço de blob
blob_service_client = BlobServiceClient.from_connection_string(
    connection_string)

# Lista todos os containers
containers_list = blob_service_client.list_containers()

# Cria uma lista vazia para armazenar todas as informações dos blobs
all_blobs_info = []

for container in containers_list:
    container_name = container.name
    container_client = blob_service_client.get_container_client(container_name)
    blobs_list = container_client.list_blobs()

    for blob in blobs_list:
        blob_name = blob.name

        if '/' in blob_name:
            folder_name = blob_name.split('/')[0]
        else:
            folder_name = ""

        all_blobs_info.append({
            'Nome do container': container_name,
            'Nome do blob': blob_name,
            'Nome da pasta': folder_name
        })

# Cria um DataFrame com as informações de todos os blobs
df = pd.DataFrame(all_blobs_info)

# Define o nome do arquivo de saída
output_dir = 'local path'
output_file_name = 'all_containers_blobs_info.xls'
output_file_path = os.path.join(output_dir, output_file_name)

# Salva o DataFrame em um arquivo xlsx usando o openpyxl engine
writer = pd.ExcelWriter(output_file_path, engine='openpyxl')
df.to_excel(writer, index=False)
writer.save()
