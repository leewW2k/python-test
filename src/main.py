from fastapi import FastAPI
from fastapi import Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse
from starlette.templating import _TemplateResponse
from src.syn_service.router import router as synServiceRouter

relative_path = "src/"

ApiClient = FastAPI()
ApiClient.include_router(synServiceRouter)

templates = Jinja2Templates(directory=(relative_path + "templates"))


@ApiClient.get('/', response_class=HTMLResponse)
async def root(request: Request) -> _TemplateResponse:
    return templates.TemplateResponse("index.html", {"request": request})
