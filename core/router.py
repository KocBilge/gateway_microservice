from fastapi import APIRouter
from routes import user_routes, product_routes, payment_routes

def include_routes(app):
    router = APIRouter()
    router.include_router(user_routes.router, prefix="/users")
    router.include_router(product_routes.router, prefix="/products")
    router.include_router(payment_routes.router, prefix="/payments")
    app.include_router(router)
