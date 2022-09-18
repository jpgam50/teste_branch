#!/bin/bash

#Este script identifica o nome do arquivo .gz criado após
#a construção do pacote e envia

FOLDER=dist
ARQUIVO=""

echo "Nome da pasta:  $FOLDER"


#verifica se o arquivo existe e se é um diretório
if [ -d $FOLDER ]; then

  # loop sobre os arquivos da pasta
  for file in $(ls $FOLDER); do

    #identifica o arquivo .gz
    if [[ $file == *.gz ]]; then
      ARQUIVO=$file
      echo "Arquivo encontrado, nome do arquivo:"
      echo "  $ARQUIVO"
    fi

  done
fi


#envia o arquivo para o servidor
curl -F package=@$"dist/$ARQUIVO" "$GEMFURRY_URL"

#verificação
echo "Endereço do servidor:  $GEMFURRY_URL"
