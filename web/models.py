from pydantic import BaseModel


class HashRequest(BaseModel):
    string: str


class HashResponse(BaseModel):
    hash_string: str | None = None
