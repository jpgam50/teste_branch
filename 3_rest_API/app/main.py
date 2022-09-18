from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from app.api import api_router


app = FastAPI(title='Api de teste para o modelo implementado')


#cria a pagina de abertura
@app.get("/")
def index(request: Request):
    """Basic HTML response."""
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Welcome to the API</h1>"
        "<div>"
        "Check the docs: <a href='/docs'>here</a>"
        "</div>"
        "</body>"
        "</html>"
    )
    return HTMLResponse(content=body)



app.include_router(api_router,
                   prefix="/teste"   #define o inicio do path do end point
                   )



#roda o API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8001, log_level="info")

    #'log_level' pode assumir os seguintes valores:    
    # -debug
    # -info
    # -warning
    # -error
    # -critical









#
