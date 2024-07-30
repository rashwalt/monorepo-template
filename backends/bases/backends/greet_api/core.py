from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backends.logs import get_logger


logger = get_logger("greet-FastAPI-logger")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root() -> dict:
    logger.info("rootが読み込まれました！")

    return {"message": "Hello World!"}
