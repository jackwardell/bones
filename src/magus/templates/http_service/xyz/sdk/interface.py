from typing import Optional
from uuid import UUID

import attr
import requests

from .config import XYZConfig
from .exceptions import FailedToCreateUserError
from .exceptions import FailedToGetUserError
from .inputs import CreateUserInput
from .inputs import GetUserInput
from .models import UserModel
from .outputs import CreateUserOutput
from .outputs import GetUserOutput
from .paths import Paths


@attr.define
class XYZSDK:
    session: requests.Session = attr.Factory(requests.Session)
    config: XYZConfig = attr.Factory(XYZConfig)

    def create_user(
        self, email_address: Optional[str], password_hash: Optional[str]
    ) -> UserModel:
        resp = self.session.get(
            self.config.url + Paths.USER,
            json=dict(
                CreateUserInput(
                    email_address=email_address,
                    password_hash=password_hash,
                )
            ),
        )
        output = CreateUserOutput(**resp.json())
        if output.success:
            return output.user
        else:
            raise FailedToCreateUserError(output.message)

    def get_user(
        self, user_id: Optional[UUID], email_address: Optional[str]
    ) -> UserModel:
        resp = self.session.get(
            self.config.url + Paths.USER,
            json=dict(
                GetUserInput(
                    user_id=user_id,
                    email_address=email_address,
                )
            ),
        )
        output = GetUserOutput(**resp.json())
        if output.success:
            return output.user
        else:
            raise FailedToGetUserError(output.message)
