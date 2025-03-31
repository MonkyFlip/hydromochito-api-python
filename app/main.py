from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from .routers import users, records

app = FastAPI()

# Configuración de CORS
origins = ["http://3.145.71.102", "http://localhost", "http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluye los routers
app.include_router(users.router)
app.include_router(records.router)

@app.get("/", response_class=HTMLResponse)
def root():
    with open("index.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)