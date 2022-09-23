
#Este script identifica o nome do arquivo .gz criado após
#a construção do pacote e envia este arquivo paro o servidor do gemfury


PATH_PROJETO=$(realpath $0)                    #caminho do script
PATH_PROJETO=${PATH_PROJETO%*/*}               #diretório do script
PATH_PROJETO=${PATH_PROJETO%*/*}               #deretório do projeto
FOLDER=${PATH_PROJETO}"/2_model_package/dist"  #diretório do arquivo .gz
ARQUIVO=""



# verifica se o arquivo existe e se é um diretório
if [ -d $FOLDER ]; then

  # loop sobre os arquivos da pasta
  for file in $(ls $FOLDER); do

    #identifica o arquivo .gz
    if [[ $file == *.gz ]]; then
      ARQUIVO=$file
      echo "Arquivo encontrado, nome do arquivo: '$ARQUIVO' "
    fi
  done

  #envia o arquivo para o servidor
  curl -F package=@"$FOLDER/$ARQUIVO" "$GEMFURRY_URL"
  echo Código de retorno da função que envia o pacote: $?
  echo Path file: "$FOLDER/$ARQUIVO"
  echo Url: "$GEMFURRY_URL"

  #Obs:as variáveis no comando curl devem estar entre "" para
  #o comando funcionar corretamente

else
  echo "Erro:pacote não enviado, o diretório '$FOLDER' não existe"
fi
