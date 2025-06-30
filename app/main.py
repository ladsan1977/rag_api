from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importa tus routers
from app.routers import drive, rag  # Agrega otros cuando los tengas: process, rag, etc.

app = FastAPI(
    title="RAG Backend API",
    version="1.0.0",
    description="Backend API para el proyecto RAG"
)

# Middleware CORS (útil para que el frontend pueda hacer peticiones sin problemas)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ Cámbialo en producción por los dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Monta los routers
app.include_router(drive.router, prefix="/drive", tags=["Drive"])
app.include_router(rag.router, prefix="/rag", tags=["RAG"])

# Endpoint raíz (útil para testeo rápido o healthcheck)
@app.get("/")
def root():
    return {"message": "RAG API is running 🚀"}
