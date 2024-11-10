import uvicorn
from typing import Annotated
from fastapi import Request, Response, status, Form
from fastapi.responses import HTMLResponse, RedirectResponse

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


@app.get("/leistungen/individual-software", response_class=HTMLResponse)
def get_service_app_development(request: Request):

    context = {
        "request": request,
        "title": "Individual-Software"
    }

    return server.templates.TemplateResponse(name="service_custom_dev.html", context=context, request=request)




@app.get("/about-us", response_class=HTMLResponse)
def get_about_us(request: Request):
    context = {
        "request": request,
        "title": "Über uns"
    }

    return server.templates.TemplateResponse(name="about_us.html", context=context, request=request)


@app.get("/kontakt", response_class=HTMLResponse)
def get_contact(request: Request):
    context = {
        "request": request,
        "title": "Kontakt"
    }

    return server.templates.TemplateResponse(name="contact.html", context=context, request=request)


@app.post("/kontakt")
async def send_contact_msg(request: Request, response: Response, anrede: Annotated[str, Form()], name: Annotated[str, Form()], email: Annotated[str, Form()], num: Annotated[str, Form()], msg: Annotated[str, Form()],):
    print({
        "anrede": anrede,
        "name": name,
        "email": email,
        "tel-num": num,
        "msg": msg
    })

    # TODO: mail handler

    response.status_code = status.HTTP_202_ACCEPTED
    return response


@app.get("/impressum", response_class=HTMLResponse)
def get_contact(request: Request):
    context = {
        "request": request,
        "title": "Impressum"
    }

    return server.templates.TemplateResponse(name="impressum.html", context=context, request=request)


@app.get("/datenschutz", response_class=HTMLResponse)
def get_contact(request: Request):
    context = {
        "request": request,
        "title": "Datenschutz"
    }

    return server.templates.TemplateResponse(name="datenschutz.html", context=context, request=request)


@app.get("/not-found", response_class=HTMLResponse)
def get_contact(request: Request):
    context = {
        "request": request,
        "title": "404 Not found"
    }

    return server.templates.TemplateResponse(name="service_custom_dev.html", context=context, request=request)


@app.get("/{full_path:path}")
def catch_all(full_path: str):
    # catches all routes not defined above.
    # any routes defined below will not be accessed since this catches it before
    return RedirectResponse(url="/not-found")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=1337, forwarded_allow_ips=["*"], proxy_headers=True)
