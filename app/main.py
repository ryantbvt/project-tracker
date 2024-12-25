from fastapi import FastAPI
from python_utils.logging import logging

from app.api.v1.router import api_router

# Initialize loger
logger = logging.init_logger()

logger.info('Starting application...')

# Intialize FastAPI
app = FastAPI(title="Project Tracker")

# Connect routers to main application
app.include_router(api_router, prefix="/v1")
