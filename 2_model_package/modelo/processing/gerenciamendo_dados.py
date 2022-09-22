import pandas as pd
from pathlib import Path
import joblib
import os

# from model import __version__ as _version
from modelo.configuracoes.config import AppConfig
from modelo.configuracoes.caminhos import DADOS_DIR,MODELO_DIR, MODEL_TREINADO_DIR


# Carrega os dados para o treinamento
def carrega_dataset(path_dados):

    df = pd.read_csv(path_dados, sep=",")
    return df


#carrega modelo
def carrega_modelo(path_modelo):
    return joblib.load(path_modelo)



def salva_modelo(modelo):
    """
    Salva uma versão do modelo e apaga todas as outras existentes. Se a versão não mudar
    o modelo salvo subscreve a existente.
    """

    # cria o diretório para salvar o modelo
    if(not os.path.isdir(MODEL_TREINADO_DIR)):
        os.mkdir(MODEL_TREINADO_DIR)


    # le a versao do pacote
    strFile= MODELO_DIR / "VERSION"
    _versao=open(strFile,).read()


    # Caminho do arquivo salvo
    nome_arquivo = f"{AppConfig.mome_pipeline_salvo}{_versao}.pkl"
    path_arquivo = MODEL_TREINADO_DIR / nome_arquivo


    # remove o arquivo existente (fornece nome)
    remove_modelos_antigos(nome_arquivo)

    # salva um novo arquivo (fornece: caminho + nome)
    joblib.dump(modelo, path_arquivo)



def remove_modelos_antigos(modelo_novo):
    """
    O App armazena somente um modelo treinado por versão. A ideia é apagar
    todas as versões existentes anteriormete e manter somenta a atual.
    Este código elimina todos os modelo menos o indicado no input.
    O indicado no input será o modelo com versão mais recente

    A função permite manter mais de um modelo se for desejado
    """

    # Modelos que devem ser mantidos
    nao_remove = [modelo_novo] + ["__init__.py"]

    # apaga todos os outros modelo
    for arq in MODEL_TREINADO_DIR.iterdir():
        if arq.name not in nao_remove:
            arq.unlink()
