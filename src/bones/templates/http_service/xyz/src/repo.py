import os
from typing import Optional
from uuid import UUID

import attr
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from .db import UserDBModel
from .domain import User
from .exceptions import UserNotCreatedError
from .exceptions import UserNotFoundError

engine = create_engine(os.environ["SQLALCHEMY_URL"])


@attr.define
class XYZRepo:
    session: Session = attr.Factory(scoped_session(sessionmaker(bind=engine)))

    def read_user(
        self, user_id: Optional[UUID], email_address: Optional[str]
    ) -> User:
        query = self.session.query(UserDBModel)
        if user_id:
            query = query.filter_by(id=str(user_id))
        if email_address:
            query = query.filter_by(email_address=email_address)
        try:
            return query.one().to_domain()
        except NoResultFound as e:
            self.session.rollback()
            raise UserNotFoundError(
                f"No user found by user_id={user_id} & "
                f"email_address={email_address}"
            ) from e

    def create_user(self, user: User) -> User:
        user_db_model = UserDBModel.from_domain(user=user)
        self.session.add(user_db_model)
        try:
            self.session.commit()
            return user_db_model.to_domain()
        except IntegrityError as e:
            self.session.rollback()
            raise UserNotCreatedError(f"User not created: {e}") from e
