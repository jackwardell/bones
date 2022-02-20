from __future__ import annotations

from uuid import UUID

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.orm import declarative_base

from .domain import User

Base = declarative_base()


class UserDBModel(Base):
    __tablename__ = "user"

    id = Column(String, primary_key=True)
    created_datetime = Column(DateTime)
    email_address = Column(String)
    password_hash = Column(String)

    def to_domain(self) -> User:
        rv = User(
            id=UUID(self.id),
            created_datetime=self.created_datetime,
            email_address=self.email_address,
            password_hash=self.password_hash,
        )
        return rv

    @classmethod
    def from_domain(cls, user: User) -> UserDBModel:
        rv = cls(
            id=str(user.id),
            created_datetime=user.created_datetime,
            email_address=user.email_address,
            password_hash=user.password_hash,
        )
        return rv
