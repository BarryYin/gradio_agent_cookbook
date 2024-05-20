from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from gradio_client import Client

client = Client("http://127.0.0.1:7860/")

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/greet/{name}")
def read_item(name: str):
    result = client.predict(
            name,	# str  in 'Name' Textbox component
            api_name="/greet"
    )
    return {"greeting": result}

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})