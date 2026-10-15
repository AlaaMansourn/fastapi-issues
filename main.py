from fastapi import FastAPI 
from app.routes.issues import router as issue_router 
from app.middleware.timer import timming_midelware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.middleware("http")(timming_midelware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(issue_router)
