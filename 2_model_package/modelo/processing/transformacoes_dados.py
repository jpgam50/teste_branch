from sklearn.base import BaseEstimator, TransformerMixin


class Mapeamento(BaseEstimator, TransformerMixin):    

    def __init__(self, variavel, mapa):
        #Parametros
        # -mapas -->lista com dicionários(mapas)
        self.variavel = variavel
        self.mapa = mapa 

    def fit(self, X, y=None):
        return self

    def transform(self, X):        
        X = X.copy()        
        X[self.variavel] = X[self.variavel].map(self.mapa)
        return X
