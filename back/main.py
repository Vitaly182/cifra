from fastapi import FastAPI
from routers.user_router import user_router


def create_app() -> FastAPI:
    app = FastAPI(
        title='Cifra',
        version='0.0.1',
    )
    app.include_router(user_router)
    return app


app = create_app