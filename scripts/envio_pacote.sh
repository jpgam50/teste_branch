
#Este script identifica o nome do arquivo .gz criado após
#a construção do pacote e envia este arquivo paro o servidor do gemfury



PATH_SCRIPT=$(realpath $"paths.sh")  #diretório do script
PATH_ROOT=${PATH_SCRIPT%*/scripts/*} #diretório raiz do projeto
PATH_MODEL_PKC=${PATH_ROOT}"/2_model_package" #diretório das pastas do projeto



#deretório do arquivo .gz
FOLDER=${PATH_MODEL_PKC}"/dist"
ARQUIVO=""


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

  #envia o arquivo para o servidor
  curl -F package=@$"dist/$ARQUIVO" "$GEMFURRY_URL"
  echo "Endereço do servidor:  $GEMFURRY_URL"

else
  echo "O diretório $FOLDER não exite"
fi
