
#Este script identifica o nome do arquivo .gz criado após
#a construção do pacote e envia este arquivo paro o servidor do gemfury


PATH_PROJETO=$(realpath $"2_model_package")  #diretório do projeto do pacote
FOLDER=${PATH_PROJETO}"/dist"                #diretório do arquivo .gz
ARQUIVO=""
GEMFURRY_URL=https://19zQZi-RplYPStzKQnuswBFV0H9z5li8@push.fury.io/joaogambaro/

#verifica se o arquivo existe e se é um diretório
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
  echo Path file: "$FOLDER/$ARQUIVO"
  echo Url: "$GEMFURRY_URL"
  #echo "$GEMFURRY_URL"
  echo Código de retorno da função que envia o pacote: $?

  #Obs:as variáveis no comando curl devem estar entre "" para
  #o comando funcionar corretamente

else
  echo "Erro:pacote não enviado, o diretório '$FOLDER' não existe"
fi
