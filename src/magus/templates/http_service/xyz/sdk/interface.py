from typing import Optional

import attr
import requests

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

    def create_user(
        self, email_address: Optional[str], password_hash: Optional[str]
    ) -> UserModel:
        resp = self.session.get(
            Paths.USER,
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
        self, user_id: Optional[int], email_address: Optional[str]
    ) -> UserModel:
        resp = self.session.get(
            Paths.USER,
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
