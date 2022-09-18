import unittest
import pandas as pd
from sklearn import metrics

from modelo.configuracoes.config import AppConfig
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

        #faz previsao
        results = preve_pipeline(df)
        y_hat = results.get("predictions")

        # transformação: dados previstos
        class_map = {0:'C', 1:'D', 2:'A', 3:'B'}
        y_hat = pd.Series(y_hat).map(class_map)

        #precisao
        prec=metrics.accuracy_score(df['class'], y_hat)

        #estatisticas com o modelo
        self.assertEqual(prec,0.7139303482587065,"A precisão não é a mesma do desenvolvimento")

        #OBS: a prcisao do modelo não é a colocada acima.
        #acho que isto aocnteeu devido a validadacao dos
        #dados pelo pydantic


    def test_prev_valores(self):

        #Teste para verificar se os valores para algumas previsões estão corretos


        #carrega os dados
        str_file=DADOS_DIR/AppConfig.nome_dados_teste
        df = carrega_dataset(str_file)

        results = preve_pipeline(df)
        y_hat = results.get("predictions")
        y_hat = pd.Series(y_hat).map({0:'C', 1:'D', 2:'A', 3:'B'})

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
