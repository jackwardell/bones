from typing import Optional
from uuid import UUID

import attr

from .domain import User
from .exceptions import UserNotFoundError
from .repo import XYZRepo


@attr.s
class XYZApp:
    repo: XYZRepo = attr.Factory(XYZRepo)

    def get_user(
        self, user_id: Optional[UUID], email_address: Optional[str]
    ) -> User:
        if not user_id and not email_address:
            raise UserNotFoundError("No params provided")

        user = self.repo.read_user(
            user_id=user_id,
            email_address=email_address,
        )
        return user

    def create_user(self, email_address: str, password_hash: str) -> User:
        user = User.create(
            email_address=email_address,
            password_hash=password_hash,
        )

        user = self.repo.save_user(user=user)
        return user
