from typing import Optional

from pydantic import BaseModel


class CreateUserInput(BaseModel):
    email_address: str
    password_hash: str


class GetUserInput(BaseModel):
    user_id: Optional[int]
    email_address: Optional[str]
