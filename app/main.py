from fastapi import FastAPI
from app.route.user_routes import router as user_router
from app.route.role_routes import router as role_router
from app.route.data_routes import router as data_router
from app.route.kpi_routes import router as kpi_router

app = FastAPI()

# Incluir las rutas
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(role_router, prefix="/roles", tags=["Roles"])
app.include_router(data_router, prefix="/data", tags=["Data"])
app.include_router(kpi_router, prefix="/kpis", tags=["KPIs"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Soluas API"}
