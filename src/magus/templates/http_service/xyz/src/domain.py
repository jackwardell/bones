from __future__ import annotations

import uuid
from datetime import datetime

import attr
from sdk.models import UserModel


@attr.define
class User:
    id: str = attr.field(validator=attr.validators.instance_of(str))
    created_datetime: datetime = attr.field(
        validator=attr.validators.instance_of(datetime)
    )
    email_address: str = attr.field(validator=attr.validators.instance_of(str))
    password_hash: str = attr.field(validator=attr.validators.instance_of(str))

    def to_model(self) -> UserModel:
        rv = UserModel(
            user_id=self.id,
            email_address=self.email_address,
            password_hash=self.password_hash,
        )
        return rv

    @classmethod
    def create(cls, email_address: str, password_hash: str) -> User:
        rv = cls(
            id=uuid.uuid4(),
            created_datetime=datetime.utcnow(),
            email_address=email_address,
            password_hash=password_hash,
        )
        return rv
