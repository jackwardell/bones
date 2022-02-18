from typing import Optional

from pydantic import BaseModel

from .models import UserModel


class CreateUserOutput(BaseModel):
    message: str
    success: bool
    user: UserModel


class GetUserOutput(BaseModel):
    message: str
    success: bool
    user: Optional[UserModel]
