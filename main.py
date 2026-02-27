from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.translate import translate_text
app = FastAPI(title="Multilingual Translator")

templates = Jinja2Templates(directory="app/templates")

LANGUAGES = [
    ("en", "English"),
    ("hi", "Hindi"),
    ("pa", "Punjabi"),
    ("te", "Telugu"),
    ("ja", "Japanese")
]

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "languages": LANGUAGES,
            "result": ""
        }
    )

@app.post("/translate", response_class=HTMLResponse)
def translate(
    request: Request,
    source_lang: str = Form(...),
    target_lang: str = Form(...),
    text: str = Form(...)
):
    result = translate_text(text, source_lang, target_lang)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "languages": LANGUAGES,
            "result": result,
            "text": text
        }
    )