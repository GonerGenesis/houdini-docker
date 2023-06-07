# houdini-docker
simple, quick and dirty setup
backend: [FastApi](https://github.com/tiangolo/fastapi), PostgreSQL, [TortoiseORM](https://github.com/tortoise/tortoise-orm), [strawberry](https://github.com/strawberry-graphql/strawberry)
frontend: [SvelteKit](https://github.com/sveltejs/kit), [Houdini](https://github.com/HoudiniGraphQL/houdini)

# prerequisites
docker compose installation

# install
run docker compose up -d in top project top directory

# running
graphiql interface: http://0.0.0.0:5001/graphql
frontend: http://localhost:5174/

# errors
the houdini watcher produces `Couldn't pull your latest schema: request to http://localhost:5001/graphql failed, reason: connect ECONNREFUSED 127.0.0.1:5001`
