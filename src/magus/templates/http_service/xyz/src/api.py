"""
todo
"""
from fastapi import FastAPI

from ..sdk.inputs import CreateUserInput
from ..sdk.inputs import GetUserInput
from ..sdk.outputs import CreateUserOutput
from ..sdk.outputs import GetUserOutput
from ..sdk.paths import Paths
from .app import XYZApp
from .exceptions import UserNotCreatedError
from .exceptions import UserNotFoundError


def api_factory(app: XYZApp = XYZApp) -> FastAPI:
    api = FastAPI()

    @api.get(Paths.USER, response_model=GetUserOutput)
    def get_user(i: GetUserInput) -> GetUserOutput:
        try:
            user = app.get_user(
                user_id=i.user_id,
                email_address=i.email_address,
            )
            output = GetUserOutput(
                message="Successfully fetched user",
                success=True,
                user=user.to_model(),
            )
            return output

        except UserNotFoundError as e:
            output = GetUserOutput(
                message=str(e),
                success=False,
                user=None,
            )
            return output

    @api.post(Paths.USER, response_model=CreateUserOutput)
    def create_user(i: CreateUserInput) -> CreateUserOutput:
        try:
            user = app.create_user(
                email_address=i.email_address,
                password_hash=i.password_hash,
            )
            output = CreateUserOutput(
                message="Successfully created user",
                success=True,
                user=user.to_model(),
            )
            return output

        except UserNotCreatedError as e:
            output = CreateUserOutput(
                message=str(e),
                success=False,
                user=None,
            )
            return output

    return api
