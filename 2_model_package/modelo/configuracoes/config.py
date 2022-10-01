#from typing import Dict, List, Sequence
#from pydantic import BaseModel
#from strictyaml import YAML, load


# Configurações da API
class AppConfig():
    nome_dados="dados_treinamento.csv"         #str
    nome_dados_teste="dados_test_pacote.csv"
    mome_pipeline_salvo= 'modelo_v'            #str


#Configurações do modelo
class ModelConfig():

    #OBS: para a classe funcionar como o autor construiu deve ser
    #colocada a funcao 'BaseModel' como herança. Para funcionar
    #como eu contrui NAO DEVE SER COLOCADA esta função como herança

    variavel_alvo='class'                     #str
    gender='gender'                           #List[str]
    gender_map = {'M': 0, 'F': 1}             #Dict[str,int]
    random_state=0                             #int
    variaveis_renomear={
        'height_cm':'heightCm',
        'weight_kg':'weightKg',
        'body fat_%':'bodyFat',
        'sit and bend forward_cm':'sitBendCm',
        'sit-ups counts':'sitUpsCounts',
        'broad jump_cm':'broadJumpCm'}

    continuous_var=['age', 'heightCm', 'weightKg', 'bodyFat', 'diastolic',
            'systolic', 'gripForce', 'sitBendCm',
            'sitUpsCounts', 'broadJumpCm']

    vari_preditivas=[
        'age',
        'heightCm',    #renomeada
        'weightKg',    #renomeada
        'bodyFat',     #renomeada
        'diastolic',
        'systolic',
        'gripForce',
        'sitBendCm',    #renomeada
        'sitUpsCounts', #renomeada
        'broadJumpCm',  #renomeada
        'gender']
