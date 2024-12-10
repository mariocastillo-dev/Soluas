from fastapi import FastAPI
from app.route.user_routes import router as user_router
from app.route.role_routes import router as role_router
from app.route.data_routes import router as data_router
from app.route.auth_routes import router as auth_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(role_router, prefix="/roles", tags=["Roles"])
app.include_router(data_router, prefix="/data", tags=["Data"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Soluas API"}