* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/api-search-provider-class.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Unity Search](https://docs.unity3d.com/6000.0/Documentation/Manual/search-overview.html)
  * [Creating a custom Search Provider](https://docs.unity3d.com/6000.0/Documentation/Manual/api.html)
  * The SearchProvider class


[](https://docs.unity3d.com/6000.0/Documentation/Manual/api.html)
Creating a custom Search Provider
[](https://docs.unity3d.com/6000.0/Documentation/Manual/api-register-provider.html)
Registering a Search Provider
# The SearchProvider class
The **[SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html)** class executes searches for specific types of items, and manages thumbnails, descriptions, and sub-filters.
It has the following basic API:
```
public class SearchProvider
{
    public SearchProvider(string id, string displayName = null);

    // Creates an Item bound to this provider.
    public SearchItem CreateItem(string id, string label = null, string description = null, Texture2D thumbnail = null);

    // Utility functions to check whether the search text matches a string.
    public static bool MatchSearchGroups(string searchContext, string content);
    public static bool MatchSearchGroups(string searchContext, string content,
                                        out int startIndex, out int endIndex);

    // The provider's unique ID.
    public NameId name;
    // Text token to "filter" a provider (for example, "me:", "p:", and "s:").
    public string filterId;
    // This provider is only active when a search explicitly specifies it with
    // its filterId.
    public bool isExplicitProvider;
    // Handler to fetch and format the label of a search item.
    public FetchStringHandler fetchLabel;
    // Handler to provide an async description for an item. Called just before
    // Search displays the item.
    // Allows a plug-in provider to fetch long descriptions only when
    // Search needs them.
    public FetchStringHandler fetchDescription;
    // Handler to provider an async thumbnail for an item. Called just before
    // Search displays the item.
    // Allows a plug-in provider to fetch/generate previews only when
    // Search needs them.
    public PreviewHandler fetchThumbnail;
    // Handler to support drag interactions. It is up to the SearchProvider
    // to properly set up the DragAndDrop manager.
    public StartDragHandler startDrag;
    // Called when the selection changes and Search can track it.
    public TrackSelectionHandler trackSelection;
    // MANDATORY: Handler to get items for a search context.
    public GetItemsHandler fetchItems;
    // A Search Provider can return a list of words that help the user complete
    // their search query.
    public GetKeywordsHandler fetchKeywords;
    // List of sub-filters that are visible in the FilterWindow for a
    // SearchProvider (see AssetProvider for an example).
    public List<NameId> subCategories;
    // Called when the Search window opens. Allows the Provider to perform
    // some caching.
    public Action onEnable;
    // Called when the Search window closes. Allows the Provider to release
    // cached resources.
    public Action onDisable;
    // Int to sort the Provider. Affects the order of search results and the
    // order in which providers are shown in the FilterWindow.
    public int priority;
    // Called when Search opens in "contextual mode". If you return true
    // it means the provider is enabled for this search context.
    public IsEnabledForContextualSearch isEnabledForContextualSearch;
}

```

## Caching and releasing resources
When you launch the Search window, it calls [`onEnable`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-onEnable.html), which you can use to cache resources.
When you close the Search window, it calls [`onDisable`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-onDisable.html), which you can use to release resources.
## Initialization
Because the Search item list uses a virtual scrolling algorithm, some [`SearchItem`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) fields (for example, [`label`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem-label.html), [`thumbnail`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem-thumbnail.html), and [`description`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem-description.html)) are fetched on demand, if they are not already provided.
To populate those fields after the items are created, you need to initialize the [`SearchProvider`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) with specific handlers ([`fetchLabel`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-fetchLabel.html), [`fetchDescription`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-fetchDescription.html), [`fetchThumbnail`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-fetchThumbnail.html)).
## Tracking item selection
You can register a callback on [`trackSelection`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-trackSelection.html) to have Search do something whenever you select an item in the search results using the mouse or the keyboard. For example, the [Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/search-assets.html)Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetWorkflow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Asset) and [Scene](https://docs.unity3d.com/6000.0/Documentation/Manual/search-scene.html)A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) providers use the [`trackSelection`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-trackSelection.html) callback to ping the selected item in Search.
## Enabling drag and drop
Some Search Providers return items that you can drag and drop into the Scene. If you are creating a custom provider whose items support drag and drop, implement [`startDrag`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-startDrag.html).
For example, the [Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/search-assets.html) and [Scene](https://docs.unity3d.com/6000.0/Documentation/Manual/search-scene.html) providers populate the `DragAndDrop` structure with the relevant item UIDs to allow proper drag and drop interactions.
## Including a provider in a contextual search
When you open the Search window with the **Alt Shift + C** shortcut, it starts a contextual search, meaning Search searches the window that has focus.
When you launch a contextual search, providers that override [`isEnabledForContextualSearch`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-isEnabledForContextualSearch.html) check to see if they should be enabled, as in the following example:
```
// Taken from Scene hierarchy provider:
// Makes the provider part of the contextual search if the Scene view or the
// Hierarchy window has focus.
isEnabledForContextualSearch = () =>
                QuickSearchTool.IsFocusedWindowTypeName("SceneView") ||
                QuickSearchTool.IsFocusedWindowTypeName("SceneHierarchyWindow");

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/api.html)
Creating a custom Search Provider
[](https://docs.unity3d.com/6000.0/Documentation/Manual/api-register-provider.html)
Registering a Search Provider
