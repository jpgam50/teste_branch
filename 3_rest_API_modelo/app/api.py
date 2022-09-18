import json
from typing import Any,Optional,List

import numpy as np
import pandas as pd
from loguru import logger
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from modelo.preve_modelo import preve_pipeline
from app import schemas
from pydantic import BaseModel

api_router = APIRouter()


class resultadoPrev(BaseModel):
    errors: Optional[Any]
    predictions: Optional[List[float]]



@api_router.post("/predict",
                response_model = resultadoPrev,  #classe retornada
                status_code=200,                 #HTTP status code(cod q informa o sucesso do request)
                )
async def predict(input_data: schemas.MultipleInputs_schemas) -> Any:

    '''
    O comentário entre aspas na função dos endpoints aparece na documentação.
    Isto é bom para descrever o que faz a função.
    '''

    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))
    results = preve_pipeline(input_df.replace({np.nan: None}))

    #Obs: a 'input_data' eh uam classe tipica do pydantic. Para
    #podermos usar esta clase como um dicionário devemos usar o
    #método para a conversão 'jsonable_encoder' conforme feito acima


    #tranforma o resultado para avalidação(de array para lista)
    results['predictions']=results['predictions'].tolist()

    logger.info(f"Tipo do resultado da previsão: {type(results.get('predictions'))}")
    logger.info(f"Resultado da previsão: {results.get('predictions')}")

    return results







#
