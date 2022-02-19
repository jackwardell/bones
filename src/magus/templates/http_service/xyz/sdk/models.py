from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class UserModel(BaseModel):
    id: UUID
    created_datetime: datetime
    email_address: str
    password_hash: str
