from fastapi import status, FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.app import init_app, session_manager
#from app.core.auth.services.middleware_auth import AuthMiddleware
from app.utils.crud.types_crud import response_message
# import templates
templates = Jinja2Templates(directory="templates")


app = init_app()

# app.add_middleware(AuthMiddleware, db_session=session_manager)    

# app.on_event("startup")

@app.get('/', response_class=HTMLResponse)
async def root(request:Request):
    return templates.TemplateResponse("index.html", {"request":request})
