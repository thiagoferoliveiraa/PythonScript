Azure Blob Storage - Lista de todos os blobs em todos os containers
Este script em Python utiliza a biblioteca azure.storage.blob para se conectar ao Azure Blob Storage e listar todos os blobs em todos os containers. Em seguida, cria um DataFrame pandas com informações de todos os blobs e salva em um arquivo xlsx usando o openpyxl engine.

Como usar
Certifique-se de ter a biblioteca azure.storage.blob instalada. Caso não tenha, instale utilizando o comando pip install azure-storage-blob.

Adicione sua connection string em connection_string.

Defina o diretório de saída em output_dir e o nome do arquivo em output_file_name.

Execute o script.

Notas
Certifique-se de ter permissões para listar os containers e blobs no Azure Blob Storage.
Este script pode levar algum tempo para ser executado, dependendo da quantidade de blobs e containers.# PythonScript
