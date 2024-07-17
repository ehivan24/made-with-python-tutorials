import functools

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from web.api import endpoints

app = FastAPI()

app.include_router(endpoints.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def validate_input(*validations):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            for i, val in enumerate(args):
                if i < len(validations):
                    if not validations[i](val):
                        raise ValueError(f"Invalid argument: {val}")
            for key, val in kwargs.items():
                if key in validations[len(args) :]:
                    if not validations[len(args) :][key](val):
                        raise ValueError(f"Invalid argument: {key}={val}")
            return await func(*args, **kwargs)

        return wrapper

    return decorator


@validate_input(lambda x: isinstance(x, int), lambda y: isinstance(y, str))
async def test_input(x, y):
    return f"{y} is {x} years old"


@app.get("/add")
async def add(x, y):
    return await test_input(x, y)


app.mount("/static", StaticFiles(directory="web/static"), name="static")
templates = Jinja2Templates(directory="web/templates")


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# @app.exception_handler(500)
# async def internal_exception_handler(request, exc: Exception):
#     s = {"error": exc, "http_status_code": 500}
#     return JSONResponse(status_code=s["http_status_code"], content=s)
