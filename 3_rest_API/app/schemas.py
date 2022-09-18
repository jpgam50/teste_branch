'''
Este arquivo contém classes pydant para a validação doss dicionários de entrada
e de saido do modelo de previsão.
'''


from typing import Any, List
from pydantic import BaseModel
from modelo.processing.validacao import VarisPrevs_schemas


#classe para validação do imput do modelo
class MultipleInputs_schemas(BaseModel):
    inputs: List[VarisPrevs_schemas]

    class Config:
        schema_extra = {
            "example": {
                'inputs':[
                    {
                        "age": 57.0,
                        "heightCm": 148.0,
                        "weightKg": 54.0,
                        "bodyFat":33.6,
                        "diastolic":78.0,
                        "systolic":135.0,
                        "gripForce":27.4,
                        "sitBendCm":18.8,
                        "sitUpsCounts":16.0,
                        "broadJumpCm":137.0,
                        "gender": "F",
                    }
                ]
            }
        }
