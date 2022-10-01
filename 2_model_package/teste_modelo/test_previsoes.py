import unittest
import pandas as pd
from sklearn import metrics

from modelo.configuracoes.config import AppConfig, ModelConfig
from modelo.preve_modelo import preve_pipeline
from modelo.processing.gerenciamendo_dados import carrega_dataset
from modelo.configuracoes.caminhos import DADOS_DIR


class TestFunc(unittest.TestCase):

    def test_prev_precisao(self):


        #Teste para verificar se a precisão dos dados previstos se mantem com a
        #implementação do modelo


        #carrega os dados
        str_file=DADOS_DIR/AppConfig.nome_dados_teste
        df = carrega_dataset(str_file)

        #renomeia as variáveis
        df = df.rename(columns=ModelConfig.variaveis_renomear)


        #faz previsao
        results = preve_pipeline(df)
        y_hat = results.get("predictions")


        #precisao
        prec=metrics.accuracy_score(df['class'], y_hat)

        #estatisticas com o modelo
        self.assertEqual(prec,0.7350746268656716,"A precisão não é a mesma do desenvolvimento")

        #OBS: a precisao do modelo não é a colocada acima.
        #acho que isto aocnteeu devido a validadacao dos
        #dados pelo pydantic


    def test_prev_valores(self):

        #Teste para verificar se os valores para algumas previsões estão corretos


        #carrega os dados
        str_file=DADOS_DIR/AppConfig.nome_dados_teste
        df = carrega_dataset(str_file)

        results = preve_pipeline(df)
        y_hat = results.get("predictions")

        #OBS: segue abaixo como era feita a separação dos dados antes.Atualmente
        #a validação dos dados é feita dentro da função 'preve_pipeline' e a
        #e com a validação também são feitas as seleções
        #var_prev=[var for var in df.columns if var not in ['Unnamed: 0','class','prev_val']]
        #X = df[var_prev]

        #verifica para 10 valores
        for i in range(10):
            self.assertEqual(y_hat[i], df['prev_val'][i], "Valor da previsao não bateu")



# ponto de entrada
if __name__=="__main__":
    unittest.main()
