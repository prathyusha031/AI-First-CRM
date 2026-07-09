from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import Base, engine
import app.models

from app.routers.interactions import router as interaction_router

app = FastAPI(
    title="AI First CRM API",
    version="1.0.0",
)

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(interaction_router)


@app.get("/")
def root():
    return {
        "status": "success",
        "message": "AI First CRM Backend Running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }