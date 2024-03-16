"""
Main Module for FastAPI Application

This module serves as the entry point for the FastAPI application. It initializes
the FastAPI instance, includes routers, and configures the application.
"""

import os 
import uvicorn

from fastapi import FastAPI

from api.v1 import api_endpoint

app = FastAPI()

app.include_router (
    api_endpoint.router,
    prefix="/api/v1",
    tags=["v1"]
)

if __name__ == "__main__":
    host = os.environ.get("LONELY_API_HOST", "0.0.0.0")
    port = int(os.environ.get("LONELY_API_PORT", 8000))
    uvicorn.run(app, host=host, port=port)
