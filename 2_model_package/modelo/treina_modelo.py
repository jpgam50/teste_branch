from sklearn.model_selection import train_test_split

from modelo.processing.gerenciamendo_dados import carrega_dataset, salva_modelo
from modelo.processing.pipeline import model_pipe


from modelo.configuracoes.config import AppConfig, ModelConfig
from modelo.configuracoes.caminhos import DADOS_DIR, MODEL_TREINADO_DIR,MODELO_DIR
from modelo.processing.validacao import valida_inputs

import joblib


def treina_pipeline():

    #carrega os dados
    str_file=DADOS_DIR/AppConfig.nome_dados
    df = carrega_dataset(str_file)

    #seleciona variaveis de treinamento e alvo
    X, erros= valida_inputs(df)
    y = df[ModelConfig.variavel_alvo]

    #OBS: para a variável X deve ser usada a função validação para ficar da
    #mesma forma como no código de previsões. Se não for feito assim, corre o
    #risco de ass variáveis de treinamento serem diferentes das variáveis usadas
    #como entrada para previsões. Neste código, por exemplo, a variáveis são
    #renomeadas na func. 'valida_inputs' de se não fosse usada esta func. a modelo
    #seria treinado com ooutros nomes de veriáveis levando a erros nas previsões.


    #Divide os dados
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.1,
                                                    random_state=0)

    #altera variável alvo
    y_train= y_train.map(ModelConfig.map_alvo)


    # OBS: ainda estou na dúvida em qual parte é melhor colocar
    # a alteração da variável alvo. Pensar se não seria melhor
    # aterar toda a tabela com os dados na hora em que os dados
    # são carregados

    # Fita o pipeline
    model_pipe.fit(X_train,y_train)

    # salva o pipeline
    salva_modelo(model_pipe)


if __name__=="__main__":
    treina_pipeline()
