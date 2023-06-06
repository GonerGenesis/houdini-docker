import dataclasses
import logging
from typing import TypeVar, Generic, Type, Optional, Any, Annotated

import strawberry
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
from tortoise import Model
from tortoise.exceptions import IntegrityError, OperationalError

from app.strawberry.base import BaseType

LOGGER = logging.getLogger(__name__)


@strawberry.type
class MsgType:
    msg: str
    id: Optional[int]
    type: Optional[str]


ModelType = TypeVar("ModelType", bound=Model)
SchemaType = TypeVar("SchemaType", bound=BaseType)
CreateSchemaType = TypeVar("CreateSchemaType", bound=object)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=object)


class StrwCRUDBase(Generic[ModelType, SchemaType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType], schema: Type[SchemaType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A Tortoise model class
        * `strawberry`: A strawberry type class
        """
        self.model = model
        self.schema = schema

    async def create(self, obj_in: CreateSchemaType) -> SchemaType:
        obj = await self._create_obj(obj_in)
        return await self.schema.from_orm(obj)

    async def _create_obj(self, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        try:
            obj = await self.model.create(**obj_in_data)
        except IntegrityError:
            raise HTTPException(status_code=401, detail=f"Sorry, that {self.model} exists.")
        return obj

    async def get(self, id: Any) -> Optional[SchemaType]:
        obj = await self.model.get(id=id)
        return await self.schema.from_orm(obj)

    async def update(self, id: Any, obj_in: UpdateSchemaType) -> Optional[SchemaType]:
        model = await self.model.get(id=id)
        dict_in = {}
        for f in dataclasses.fields(obj_in):
            LOGGER.info(f)
            if getattr(obj_in, f.name):
                dict_in[f.name] = getattr(obj_in, f.name)

        model.update_from_dict(dict_in)
        await model.save()
        return await self.schema.from_orm(await self.model.get(id=id))

    async def delete(self, id: Any) -> Optional[MsgType]:
        model: ModelType = await self.model.get(id=id)
        LOGGER.info("delete: ", dict(model))
        try:
            await model.delete()
        except OperationalError:
            raise HTTPException(status_code=404, detail=f"{self.model.__name__} {id} not found")
        return MsgType(msg=f"Deleted {self.model.__name__} {id}", id=id, type=self.model.__name__)