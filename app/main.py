import uvicorn

from fastapi import FastAPI, HTTPException, Request, Response, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse

import app.utils.app_setup as server

app = server.app


@app.get("/", response_class=HTMLResponse)
def get_homepage(request: Request):
    context = {
        "request": request,
        "title": "Herzlich Willkommen!"
    }

    return server.templates.TemplateResponse(name="home.html", context=context, request=request)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=1337, forwarded_allow_ips=["*"], proxy_headers=True)
