from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from modelo.processing.transformacoes_dados import Mapeamento
from modelo.processing.transformacoes_dados import transf_yeo_johnson
from modelo.configuracoes.config import AppConfig, ModelConfig



# Cosntrução do pipeline
model_pipe= Pipeline([
    ('map_gender', Mapeamento(variavel='gender',mapa=ModelConfig.gender_map)),
    ('YeoYohnson_trans', transf_yeo_johnson(ModelConfig.continuous_var)),
    ('randForest', RandomForestClassifier(max_depth=14,
                             max_features=8,
                             n_estimators=80,
                             bootstrap=True,
                             max_samples=None,
                             random_state=0))
])
