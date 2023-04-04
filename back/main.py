from fastapi import FastAPI
from fastapi_pagination import add_pagination

from routers.user_router import user_router
from middlewares import RedisMiddleware
from config import get_settings


# async def startup_event():
#     print('App was started!')

def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title='Cifra',
        version='0.0.1',
    )
    # app.on_event("startup")(startup_event)
    app.include_router(user_router)
    app.add_middleware(RedisMiddleware, settings=settings)
    add_pagination(app)
    return app

