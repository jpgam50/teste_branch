from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import PowerTransformer


class Mapeamento(BaseEstimator, TransformerMixin):

    def __init__(self, variavel, mapa):
        '''
        variavel: nome da coluna que será alterada
        mapa: mapa com as alterações
        '''
        self.variavel = variavel
        self.mapa = mapa


    def fit(self, X, y=None):
        '''
        X: dataframe com os dados de treinamento
        y: serie com o rótulos do dados de treinamento
        '''
        return self


    def transform(self, X):
        '''
        X: dataframe com os dados de treinamento
        '''
        X = X.copy()
        X[self.variavel] = X[self.variavel].map(self.mapa)
        return X





class transf_yeo_johnson(BaseEstimator, TransformerMixin):

    def __init__(self, colunas):
        '''
        colunas: lista com as colunas que serão transformadas
        '''
        self.colunas = colunas
        self.obj_transf= PowerTransformer(method="yeo-johnson")


    def fit(self, X, y=None):
        '''
        X: dataframe com os dados de treinamento
        y: serie com o rótulos do dados de treinamento
        '''
        self.obj_transf= self.obj_transf.fit(X[self.colunas].values)
        return self


    def transform(self, X):
        '''
        X: dataframe com os dados de treinamento
        '''
        X = X.copy()
        X_array = X[self.colunas].values
        X[self.colunas] = self.obj_transf.transform(X_array)
        return X
