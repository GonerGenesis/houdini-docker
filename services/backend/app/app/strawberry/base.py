import dataclasses
import logging
from typing import TypeVar, Type

import strawberry
import tortoise.models
from tortoise.fields import ReverseRelation, ForeignKeyRelation
from tortoise.queryset import QuerySet

logger = logging.getLogger(__name__)

T = TypeVar('T', bound='BaseType')
ModelType = TypeVar('ModelType', bound=tortoise.Model)
@strawberry.type
class BaseType:

    @classmethod
    async def from_orm(cls: Type[T], orm_model: ModelType) -> T:
        filtered_dict = {}
        if dataclasses.is_dataclass(cls):
            for f in dataclasses.fields(cls):
                attribute = getattr(orm_model, f.name)
                if isinstance(attribute, dict):
                    attribute = f.type(**attribute)
                if isinstance(attribute, (ReverseRelation, QuerySet)):
                    attribute = await attribute.all()

                filtered_dict[f.name] = attribute