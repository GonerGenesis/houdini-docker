from typing import Tuple, Any, Optional, Union, Type, List

from tortoise import fields, Model
from tortoise.validators import MinLengthValidator

class User(Model):
    id = fields.IntField(pk=True, unique=True)
    username = fields.CharField(max_length=20, unique=True, validators=[MinLengthValidator(1)])