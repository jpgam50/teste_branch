from fastapi import FastAPI
from app.api import api_router



app = FastAPI(title='Api de teste para o modelo implementado')


app.include_router(api_router,
                   prefix="/teste"   #define o inicio do path do end point
                   )



#roda o API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8001, log_level="info")

    #'log_level' pode assumir os seguintes valores:
    # -trace
    # -debug
    # -info
    # -warning
    # -error
    # -critical









#
