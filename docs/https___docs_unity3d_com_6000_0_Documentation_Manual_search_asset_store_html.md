* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/search-asset-store.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity Search](https://docs.unity3d.com/6000.0/Documentation/Manual/search-overview.html)
  * [Search Providers](https://docs.unity3d.com/6000.0/Documentation/Manual/search-providers.html)
  * Search the Unity Asset Store


[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-packages.html)
Search for packages
[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-additional-searchfilters.html)
Additional Search filters
# Search the Unity Asset Store
The **Asset Store** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AssetStore) Search Provider searches the [Unity Asset Store](https://assetstore.unity.com/). The Preview **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) displays a preview of each item. Open the Asset Store to see more information about an Asset, such as its name, price, publisher, and category.
**NOTE:** This search requires a search token to execute it. You cannot make it an [active Search Provider](https://docs.unity3d.com/6000.0/Documentation/Manual/search-filters.html#persistent-search-filters), or combine it with other Search Providers.
**[Search token](https://docs.unity3d.com/6000.0/Documentation/Manual/search-filters.html#search-tokens):** `store:`
**[Default action](https://docs.unity3d.com/6000.0/Documentation/Manual/search-usage.html#default-actions):** Opens the Unity Asset Store web site to the Asset’s page.
**[Context menu actions](https://docs.unity3d.com/6000.0/Documentation/Manual/search-usage.html#additional-actions):**
Action: | Function:  
---|---  
**Open Unity Asset Store** | Opens the Unity Asset Store web site to the Asset’s page.  
![Search results from the Asset Store](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/search-provider-asset-store.png)  
_Asset Store Search Provider_
## Sub-filters
Use these tokens to limit your search results.
Filter | Search token | Description  
---|---|---  
**Minimum price** | `store: min_price:number` |  `store: min_price:5 bolt`  
  
Searches for Assets with a minimum price of 5$ and the word `bolt` in their name.  
**Maximum price** | `store: max_price:number` |  `store: max_price:5 bolt`  
  
Searches for Assets with a maximum price of 5$ and the word `bolt` in their name.  
**Publisher** | `store: publisher:name` |  `store: publisher:Gargore`  
  
Searches for Assets published by the company Gargore. Note that the publisher name must be exact.  
**Version** | `store: version:number` |  `store: version:2017`  
  
Searches for Assets that minimally support Unity 2017.  
**Free** | `store: free:boolean` |  `store: free:true asteroid`  
  
Searches for Assets that are free and that have the word `asteroid` in their name.  
**On sale** | `store: on_sale:boolean` |  `store: on_sale:true max_price:5`  
  
Searches for Assets that are on sale and that have a max price of 5$.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-packages.html)
Search for packages
[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-additional-searchfilters.html)
Additional Search filters
