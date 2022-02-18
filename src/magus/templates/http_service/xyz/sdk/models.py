from pydantic import BaseModel


class UserModel(BaseModel):
    user_id: int
    email_address: str
    password_hash: str
