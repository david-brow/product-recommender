from fastapi import FastAPI
from .routers import products, recommendations
from .database import init_db

app = FastAPI()

# Initialize the database
init_db()

# Include routers
app.include_router(products.router, prefix="/api")
app.include_router(recommendations.router, prefix="/api")
