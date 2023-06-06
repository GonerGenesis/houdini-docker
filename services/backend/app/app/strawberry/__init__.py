import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.subscriptions import GRAPHQL_TRANSPORT_WS_PROTOCOL, GRAPHQL_WS_PROTOCOL
from app.strawberry.utils import get_context

from app.strawberry.user import UserType, UserInput, UserUpdate


@strawberry.type
class Query:
    from app.strawberry.functions.user import get_user


@strawberry.type
class Mutation:
    from app.strawberry.functions.user import create_user


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context,
    subscription_protocols=[
        GRAPHQL_TRANSPORT_WS_PROTOCOL,
        GRAPHQL_WS_PROTOCOL,
    ],
)