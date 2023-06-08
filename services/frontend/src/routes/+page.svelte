<script lang="ts">
	import { Client, setContextClient, cacheExchange, fetchExchange, queryStore, gql } from '@urql/svelte';

	const client = new Client({
		url: 'http://localhost:5001/graphql',
		exchanges: [cacheExchange, fetchExchange]
	});

	const user = queryStore({
    client: client,
    query: gql`
      query {
        getUser(id: 1) {
          id
          username
        }
      }
    `,
  });
</script>

<h1 class="text-3xl font-bold underline">
	Welcome to SvelteKit {$user.data?.getUser.username}
</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
