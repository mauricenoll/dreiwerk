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


@app.get("/tech-stack", response_class=HTMLResponse)
def get_homepage(request: Request):
    context = {
        "request": request,
        "title": "Unser TechStack"
    }

    return server.templates.TemplateResponse(name="tech_stack.html", context=context, request=request)


@app.get("/leistungen/", response_class=HTMLResponse)
def get_services(request: Request):
    context = {
        "request": request,
        "title": "Unsere Services"
    }

    return server.templates.TemplateResponse(name="services.html", context=context, request=request)


@app.get("/leistungen/web-entwicklung", response_class=HTMLResponse)
def get_service_web_development(request: Request):
    context = {
        "request": request,
        "title": "Webentwicklung"
    }

    return server.templates.TemplateResponse(name="service_webdev.html", context=context, request=request)


@app.get("/leistungen/app-entwicklung", response_class=HTMLResponse)
def get_service_app_development(request: Request):
    context = {
        "request": request,
        "title": "Appentwicklung"
    }

    return server.templates.TemplateResponse(name="service_appdev.html", context=context, request=request)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=1337, forwarded_allow_ips=["*"], proxy_headers=True)
