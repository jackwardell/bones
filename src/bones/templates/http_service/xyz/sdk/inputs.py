from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class CreateUserInput(BaseModel):
    email_address: str
    password_hash: str


class GetUserInput(BaseModel):
    user_id: Optional[UUID]
    email_address: Optional[str]
