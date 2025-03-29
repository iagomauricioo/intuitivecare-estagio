from typing import Union, List, Dict
from fastapi import FastAPI, HTTPException
import pandas as pd
import os
import numpy as np
from api.v1.routers import api_router

app = FastAPI()
app.include_router(api_router, prefix="/api/v1")