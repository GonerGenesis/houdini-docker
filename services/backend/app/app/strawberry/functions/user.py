import logging
from app.strawberry.msg import MsgType

import strawberry
from app.db import User
from app.strawberry import UserType, UserInput, UserUpdate
from app.strawberry.functions.strw_base import StrwCRUDBase
logger = logging.getLogger(__name__)


class CRUDuser(StrwCRUDBase[User, UserType, UserInput, UserUpdate]):
    pass


crud_user = CRUDuser(User, UserType)

@strawberry.field
async def get_user(self, id: int) -> UserType:
    return await crud_user.get(id=id)

@strawberry.mutation
async def create_user(self, user: UserInput) -> UserType:
    # settings: Settings = info.context['settings']
    user_obj = await crud_user.create(user)
    return user_obj

@strawberry.mutation
async def update_user(self, user_id: int, user: UserUpdate) -> UserType:
    user = await crud_user.update(id=user_id, obj_in=user)
    return user


@strawberry.mutation
async def delete_user(self, id: int) -> MsgType:
    return await crud_user.delete(id=id)