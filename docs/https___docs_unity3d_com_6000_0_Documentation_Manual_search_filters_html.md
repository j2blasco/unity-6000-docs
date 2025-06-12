* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/search-filters.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity Search](https://docs.unity3d.com/6000.0/Documentation/Manual/search-overview.html)
  * [Search usage](https://docs.unity3d.com/6000.0/Documentation/Manual/search-usage.html)
  * Filter searches


[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-usage.html)
Search usage
[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-query-operators.html)
Search query operators
# Filter searches
Filtering narrows the scope of your searches to specific providers. You can filter searches in the following ways:
  * Set up persistent search filters to control which providers Search uses for regular searches.
  * Use a Search Provider’s search token in the search field to only display results from that provider.
  * Limit your search results by using sub-filters and [query operators](https://docs.unity3d.com/6000.0/Documentation/Manual/search-query-operators.html) and using the [keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/search-index-manager.html#index-results) available for your index.
  * See a list of additional search filters [here](https://docs.unity3d.com/6000.0/Documentation/Manual/search-additional-searchfilters.html).


## Persistent search filters
You can temporarily toggle Search Providers on and off from the Filters pane. This can help reduce the number of items that a search returns, which is convenient if you already know what type of item you are looking for. The providers that are toggled on at any given time are the active Search Providers.
![The More menu showing the list of active and inactive search providers](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/search-filter-search-providers-1.png) The More menu showing the list of active and inactive search providers
To set persistent search filters:
  1. In the main menu, go to **Edit** > **Search** > **Search All** to launch Search.
  2. In the Search Providers area select **More Options** (**⋮**)
  3. Enable or disable any Search Providers you want to include/exclude from subsequent searches.


## Search tokens
Every Search Provider has a unique text string called a search token, also called a filter ID. When you prefix a search query with a provider’s search token, Search limits the scope of the search to that provider.
For example, `p:` is the search token for the Asset Search Provider. When you enter `p:Player` in the search field, Search searches for Assets that match the term “Player” (for example, assets with “Player” in their names).
See [Search Providers](https://docs.unity3d.com/6000.0/Documentation/Manual/search-providers.html) for a list of search tokens for Search Providers.
See [Additional search tokens](https://docs.unity3d.com/6000.0/Documentation/Manual/search-additional-searchfilters.html) for a list of search tokens for **Prefabs** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab), Files, Types, Properties, and Dependencies searches.
## Combining search tokens
You can combine search tokens to create more complex queries.
  * The queries are written on one line with one character space between tokens.
  * The character space between each new token is an “And” operation, so both filters must be true for the query to return a result. Add another [operator](https://docs.unity3d.com/6000.0/Documentation/Manual/search-query-operators.html) (or, <, >) to return different results.
  * If a Search Provider filter token (h:, p:) is used, it must be the first component in the query.


Here are a few examples:
Query | Description  
---|---  
`h: t:meshrenderer p(castshadows)!="Off"` | Searches all static meshes in a **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) that cast a shadow.  
`h: t:light p(color)=#FFFFFF p(intensity)>7.4` | Searches all lights in a Scene with a specific color with brightness higher than 7.4.  
`h: path:/Collectables t:collectable` | Find all objects with a component `Collectable` located in the path `/Collectables.`  
## Search expressions
Search expressions allow you to add to the search query language to express complex queries that cross-reference multiple providers, for example, to search for all objects in a scene that use a **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) that doesn’t compile. See [Search expressions](https://docs.unity3d.com/6000.0/Documentation/Manual/search-expressions.html) for more information.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-usage.html)
Search usage
[](https://docs.unity3d.com/6000.0/Documentation/Manual/search-query-operators.html)
Search query operators
