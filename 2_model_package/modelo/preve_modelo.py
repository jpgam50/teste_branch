from modelo.processing.gerenciamendo_dados import carrega_modelo
from modelo.configuracoes.config import AppConfig
from modelo.configuracoes.caminhos import MODEL_TREINADO_DIR
from modelo.processing.validacao import valida_inputs


def preve_pipeline(dados):
    #duvidas:
    #-é necessário importar a biblioteca pandas para esta funcao funcionar
    #-se não for, compensa importar so pra colocar o tipo de dado no inputs
    # da função

    #Inputs:
    # X-> dataframe contendo os dados

    #carrega modelo treinado
    str_model=str(MODEL_TREINADO_DIR/AppConfig.mome_pipeline_salvo)+"1.0.0.pkl"
    modelo=carrega_modelo(str_model)

    #valida dados
    dados, erros= valida_inputs(dados)

    results = {
            "predictions": None,
            "errors": None,
            #"version": _version,
            }

    #previsão com o modelo
    results = {
        "predictions": modelo.predict(dados),
        "errors": erros,
        #"version": _version,
        }

    return results


if  __name__=="__main__":

    from modelo.processing.gerenciamendo_dados import carrega_dataset
    from modelo.configuracoes.caminhos import DADOS_DIR
    from modelo.configuracoes.config import AppConfig

    #carrega os dados
    str_file=DADOS_DIR/AppConfig.nome_dados_teste
    df = carrega_dataset(str_file)

    #faz previsao
    results = preve_pipeline(df)
    print("Previsões: ",results['predictions'])
    print("Erros: ", results['errors'])





    
