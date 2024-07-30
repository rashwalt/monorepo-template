from fastapi import Body, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backends import logs, messages
from backends.schemas import Message


logger = logs.get_logger("message-FastAPI-logger")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/message/", response_model=int)
def create(content: str = Body()):
    logger.info(f'メッセージ作成: content={content}')

    return messages.create(content)


@app.get("/message/{message_id}", response_model=Message)
def read(message_id: int):
    logger.info(f'メッセージ取得: id={message_id}')

    return messages.read(message_id)


@app.put("/message/{message_id}", response_model=None)
def update(message_id: int, content: str = Body()):
    logger.info(f'メッセージ更新: id={message_id}')

    return messages.update(message_id, content)


@app.delete("/message/{message_id}", response_model=None)
def delete(message_id: int):
    logger.info(f'メッセージ削除: id={message_id}')

    return messages.delete(message_id)
