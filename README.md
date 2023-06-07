# houdini-docker
simple, quick and dirty setup
backend: [FastApi](https://github.com/tiangolo/fastapi), PostgreSQL, [TortoiseORM](https://github.com/tortoise/tortoise-orm), [strawberry](https://github.com/strawberry-graphql/strawberry)
frontend: [SvelteKit](https://github.com/sveltejs/kit), [Houdini](https://github.com/HoudiniGraphQL/houdini)

# prerequisites
docker compose installation

# install
run `docker compose up -d` in top project top directory

# access
graphiql interface: http://0.0.0.0:5001/graphql
frontend: http://localhost:5174/

# errors
houdini can't find 0.0.0.0 or localhost. Although it is possible to ping (docker compose exec frontend ping 0.0.0.0:5001) the graphql backend from the frontend docker container. That kind of problem didn't appeared with urql before.

# workaround 
running the frontend directly on the localhost works like a charm
