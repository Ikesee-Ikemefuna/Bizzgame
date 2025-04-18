from fastapi import status, FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.app import init_app, session_manager
#from app.core.auth.services.middleware_auth import AuthMiddleware
from app.utils.crud.types_crud import response_message

app = FastAPI();
app.mount("/static", StaticFiles(directory="static"), name="static")

templates=Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def root(request:Request):
    return templates.TemplateResponse("index.html", {"request":request})
