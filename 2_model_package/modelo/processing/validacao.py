from typing import List, Optional, Tuple
from pydantic import BaseModel, ValidationError
import numpy as np
import pandas as pd


from modelo.configuracoes.config import ModelConfig


class VarisPrevs_schemas(BaseModel):
    age: Optional[float]
    heightCm: Optional[float]
    weightKg: Optional[float]
    bodyFat: Optional[float]
    diastolic: Optional[float]
    systolic: Optional[float]
    gripForce: Optional[float]
    sitBendCm: Optional[float]
    sitUpsCounts: Optional[float]
    broadJumpCm: Optional[float]
    gender: Optional[str]


class MultipleInputs_schemas(BaseModel):
    inputs: List[VarisPrevs_schemas]



def valida_inputs(dados: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:

    #Inputs
    #'dados'-> dataframe como os dados, este df contém todas as variáveis
    #          incluindo a variável alvo. A validação é que é responsável por
    #          selecionar as variáveis de interesse de acordo com classe pydantic

    # altera os dados
    dados.rename(columns= ModelConfig.variaveis_renomear, inplace=True) #renomeia variaveis
    dados_preditivos = dados[ModelConfig.vari_preditivas]         #colunas dos dados preditivos
    #OBS: usando pydantic a linha de cima não é necessária. Mantive pq o autor
    #do original escreveu, mas não precisa


    errors = None
    teste= None
    try:

        #valida os dados usando uma classe pydantic
        dados_validados=MultipleInputs_schemas(
            inputs=dados_preditivos.replace({np.nan: None}).to_dict(orient="records")
        )
    except ValidationError as error:
        errors = error.json()


    #transforma os dados validados em DataFrame
    dados_validados=dados_validados.dict()
    dados_validados=dados_validados['inputs']
    dados_validados=pd.DataFrame(dados_validados)

    return dados_validados, errors







if __name__=='__main__':

    from modelo.configuracoes.caminhos import DADOS_DIR
    from modelo.configuracoes.config import AppConfig
    from modelo.processing.gerenciamendo_dados import carrega_dataset

    str_file=DADOS_DIR/AppConfig.nome_dados_teste
    df = carrega_dataset(str_file)
    print()

    #função em contrução
    a,b=valida_inputs(dados=df)
    print(a)
