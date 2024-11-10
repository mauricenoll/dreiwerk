from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    # no wildcards here not allowed with allow_credentials = True; more can be added
    allow_methods=["GET", "OPTIONS", "POST"],
    # no wildcards are also better here
    allow_headers=["Access-Control-Allow-Headers", 'Content-Type', 'Authorization', 'Access-Control-Allow-Origin'],

)

app.mount("/css/mobile", StaticFiles(directory="static/css/mobile"), name="mobile")
app.mount("/css/desktop", StaticFiles(directory="static/css/desktop"), name="desktop")
app.mount("/css", StaticFiles(directory="static/css"), name="css")
app.mount("/js", StaticFiles(directory="static/js"), name="js")
app.mount("/fonts", StaticFiles(directory="static/fonts"), name="fonts")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")
templates = Jinja2Templates(directory="template")
