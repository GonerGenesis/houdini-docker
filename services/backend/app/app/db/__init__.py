from tortoise import Tortoise

from .models import User

Tortoise.init_models(["app.db.models"], "models")