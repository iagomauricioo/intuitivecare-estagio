from typing import Union, List, Dict
from fastapi import FastAPI, HTTPException
import pandas as pd
import os
import numpy as np
from api.v1.routers import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(api_router, prefix="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens (desativa o CORS)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)
