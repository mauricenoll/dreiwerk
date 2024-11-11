import os

import uvicorn
from typing import Annotated
from fastapi import Request, Response, status, Form
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
import mail_handler
from mail_templates import contact_template
import utils.app_setup as server
from smtplib import SMTPRecipientsRefused, SMTPSenderRefused, SMTPDataError, SMTPNotSupportedError, SMTPHeloError

app = server.app


# fixme: to header problem with emails
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
async def send_contact_msg(request: Request, response: Response, anrede: Annotated[str, Form()],
                           name: Annotated[str, Form()], email: Annotated[str, Form()], num: Annotated[str, Form()],
                           msg: Annotated[str, Form()], data_protection: Annotated[bool, Form()]):
    form_data = {
        "anrede": anrede,
        "name": name,
        "email": email,
        "tel-num": num,
        "msg": msg,
        "data_protection": data_protection
    }
    handler = mail_handler.EmailHandler(myEmail=os.getenv("INFO_EMAIL"), password=os.getenv("INFO_PASSWORD"),
                                        mailHost=os.getenv("MAIL_HOST"), port=int(os.getenv("MAIL_PORT")))
    try:
        handler.send_mail(email, contact_template.get_contact_mail_template(name), form_data)
        response.status_code = status.HTTP_202_ACCEPTED
    except SMTPDataError and SMTPHeloError and SMTPNotSupportedError and SMTPSenderRefused and SMTPRecipientsRefused:
        response.status_code = status.HTTP_400_BAD_REQUEST

    return response


@app.get("/anfrage", response_class=HTMLResponse)
def get_inquiry(request: Request):
    context = {
        "request": request,
        "title": "Projektanfrage"
    }

    return server.templates.TemplateResponse(name="inquiry.html", context=context, request=request)


@app.post("/anfrage")
async def send_inquiry_msg(request: Request, response: Response, anrede: Annotated[str, Form()],
                           name: Annotated[str, Form()],
                           email: Annotated[str, Form()], num: Annotated[str, Form()], msg: Annotated[str, Form()],
                           data_protection: Annotated[bool, Form()], business: Annotated[str, Form()],
                           branche: Annotated[str, Form()],
                           budget: Annotated[str, Form()], interest: Annotated[str, Form()]
                           ):
    form_data = {
        "anrede": anrede,
        "name": name,
        "email": email,
        "tel-num": num,
        "msg": msg,
        "business": business,
        "branche": branche,
        "budget": budget,
        "interest": interest,
        "data_protection": data_protection
    }

    handler = mail_handler.EmailHandler(myEmail=os.getenv("INFO_EMAIL"), password=os.getenv("INFO_PASSWORD"),
                                        mailHost=os.getenv("MAIL_HOST"), port=int(os.getenv("MAIL_PORT")))
    try:
        handler.send_mail(email, contact_template.get_contact_mail_template(name), form_data)
        response.status_code = status.HTTP_202_ACCEPTED
    except SMTPDataError and SMTPHeloError and SMTPNotSupportedError and SMTPSenderRefused and SMTPRecipientsRefused:
        response.status_code = status.HTTP_400_BAD_REQUEST

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
        "title": "Seite konnte nicht gefunden werden"

    }

    return server.templates.TemplateResponse(name="not_found.html", context=context, request=request)


@app.get("/{full_path:path}")
def catch_all(full_path: str):
    # catches all routes not defined above.
    # any routes defined below will not be accessed since this catches it before
    if "wp-includes" in full_path or ".env" in full_path or ".git" in full_path or ".php" in full_path:
        return RedirectResponse(url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')  # rickroll these fuckers

    return RedirectResponse(url="/not-found")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=1337, forwarded_allow_ips=["*"], proxy_headers=True)
