import { createClient } from 'graphql-ws'
import { HoudiniClient, subscription } from '$houdini';

export default new HoudiniClient({
    url: "http://0.0.0.0:5001/graphql",
    plugins: [
        subscription(() => createClient({
          url: 'ws://localhost:5001/graphql'
        }))
      ]

    // uncomment this to configure the network call (for things like authentication)
    // for more information, please visit here: https://www.houdinigraphql.com/guides/authentication
    // fetchParams({ session }) { 
    //     return { 
    //         headers: {
    //             Authentication: `Bearer ${session.token}`,
    //         }
    //     }
    // }
})
