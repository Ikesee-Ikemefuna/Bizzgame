from fastapi import status, FastAPI
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.requests import Request

from app.app import init_app, session_manager
#from app.core.auth.services.middleware_auth import AuthMiddleware
from app.utils.crud.types_crud import response_message
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app=FastAPI()

templates=Jinja2Templates(directory="templates");

# app.add_middleware(AuthMiddleware, db_session=session_manager)    

app.mount("/static", StaticFiles(directory="static"), name="static")
# app.on_event("startup")

@app.get("/")
async def index(request:Request):
   return templates.TemplateResponse("index.html", {"request":request})