from feature_engine.transformation import YeoJohnsonTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from modelo.processing.transformacoes_dados import Mapeamento
from modelo.configuracoes.config import AppConfig, ModelConfig


#DUVIDA: para importar a funcão Mapeamento, foi necessário importar
#de "processing.transformacoes_dados" ao invez de somente "transformacoes_dados".
#Não entendi o pq disto, já que este script também está na pasta 'processing'.


# Cosntrução do pipeline
model_pipe= Pipeline([
    ('YeoYohnson_trans',YeoJohnsonTransformer(variables = ModelConfig.continuous_var)),

    ('map_gender',Mapeamento(variavel=ModelConfig.gender,
                             mapa=ModelConfig.gender_map)),

    ('randForest', RandomForestClassifier(n_estimators=50,
                             max_depth=24,
                             max_features=5,
                             bootstrap=True,
                             max_samples=None,
                             random_state=ModelConfig.random_state))
])
