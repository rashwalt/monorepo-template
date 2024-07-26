from pydantic import BaseModel, ConfigDict


class Message(BaseModel):
    id: int | None
    content: str | None = None

    model_config = ConfigDict(from_attributes=True)
