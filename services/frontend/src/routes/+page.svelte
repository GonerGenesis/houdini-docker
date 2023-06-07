<script lang="ts">
    import type { PageData } from './$houdini'
    export let data: PageData

    // pull the store reference from the route props
    $: ({ UserInfo } = data)
    $: console.log($UserInfo.data)
</script>

<h1 class="text-3xl font-bold underline">Welcome to SvelteKit {$UserInfo.data?.getUser.username} </h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
