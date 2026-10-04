"""
Main entry point for EduTrack AI application.
Hosts FastAPI backend, Swagger docs, and serves responsive frontend.
"""
import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.database import init_db
from backend.seed import run_seed
from backend.routers import auth_routes, subject_routes, task_routes, dashboard_routes

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize SQLite database and tables on startup
    init_db()
    # Ensure demo user and data are seeded idempotently
    run_seed()
    yield

app = FastAPI(
    title="EduTrack AI — Assistente Educacional Personalizado",
    description="API RESTful para gestão de disciplinas, tarefas acadêmicas, cálculo de progresso ponderado e recomendações inteligentes.",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware for development and external clients
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Routers
app.include_router(auth_routes.router)
app.include_router(subject_routes.router)
app.include_router(task_routes.router)
app.include_router(dashboard_routes.router)

@app.get("/api/health", tags=["Sistema"])
def health_check():
    return {"status": "ok", "app": "EduTrack AI", "version": "1.0.0"}

# Frontend static files mounting
frontend_path = os.path.join(os.path.dirname(__file__), "frontend")
if os.path.exists(frontend_path):
    # Serve assets under static paths if they exist
    app.mount("/static", StaticFiles(directory=frontend_path), name="static")

    @app.get("/", include_in_schema=False)
    def serve_frontend_index():
        index_file = os.path.join(frontend_path, "index.html")
        if os.path.exists(index_file):
            return FileResponse(index_file)
        return {"message": "Frontend index.html não encontrado."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
