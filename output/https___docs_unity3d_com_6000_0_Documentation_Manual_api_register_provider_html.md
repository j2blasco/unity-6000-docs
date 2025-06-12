* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/api-register-provider.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity Search](https://docs.unity3d.com/6000.0/Documentation/Manual/search-overview.html)
  * [Creating a custom Search Provider](https://docs.unity3d.com/6000.0/Documentation/Manual/api.html)
  * Registering a Search Provider


[](https://docs.unity3d.com/6000.0/Documentation/Manual/api-search-provider-class.html)
The SearchProvider class
[](https://docs.unity3d.com/6000.0/Documentation/Manual/api-searching.html)
Performing a search
# Registering a Search Provider
To add a new Search Provider, create a function and tag it with the [`SearchItemProvider`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItemProviderAttribute.html) attribute, as in the following example:
```
[SearchItemProvider]
internal static SearchProvider CreateProvider()
{
    return new SearchProvider(type, displayName)
    {
        filterId = "me:",
        fetchItems = (context, items, provider) =>
        {
            var itemNames = new List<string>();
            var shortcuts = new List<string>();
            GetMenuInfo(itemNames, shortcuts);

            items.AddRange(itemNames.Where(menuName =>
                    SearchProvider.MatchSearchGroups(context.searchText, menuName))
                .Select(menuName => provider.CreateItem(menuName,
                                            Path.GetFileName(menuName), menuName)));
        },

        fetchThumbnail = (item, context) => Icons.shortcut
    };
}

```

  * The function must return a new `SearchProvider` instance.
  * The `SearchProvider` instance must have the following:
  * A unique `type`. For example, **Asset** , **Menu** , or ****Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene)**.
  * A `displayName` to use in the [Filters pane](https://docs.unity3d.com/6000.0/Documentation/Manual/search-filters.html#persistent-search-filters).
  * The optional `filterId` provides a search token for [text-based filtering](https://docs.unity3d.com/6000.0/Documentation/Manual/search-filters.html#search-tokens). For example, `p:` is the filter ID for [Asset searches](https://docs.unity3d.com/6000.0/Documentation/Manual/search-assets.html).


## Registering a Search Provider shortcut
To register a shortcut for a new provider, use:
```
[UsedImplicitly, Shortcut("Help/Quick Search/Assets")]
private static void PopQuickSearch()
{
    // Open Search with only the "Asset" provider enabled.
    SearchService.ShowContextual("asset");
}

```

You can map shortcuts to keys or key combinations using the [shortcuts manager](https://docs.unity3d.com/Manual/ShortcutsManager.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/api-search-provider-class.html)
The SearchProvider class
[](https://docs.unity3d.com/6000.0/Documentation/Manual/api-searching.html)
Performing a search
