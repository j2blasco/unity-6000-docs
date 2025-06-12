* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html

# SearchProvider
class in UnityEditor.Search
Leave feedback
  

Implements interfaces:[ISerializationCallbackReceiver](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ISerializationCallbackReceiver.html)
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
SearchProvider manages search for specific types of items and manages all fields of a SearchItem such as thumbnails, descriptions, subfilters.
A first example that allows to search for specific prefabs and insert them in the scene.
```
using System.Collections.Generic;
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class TreeSearchProvider
{
    internal static string id = "example_tree";

    [SearchItemProvider]
    internal static SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) CreateProvider()
    {
        return new SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html)("example_tree", "Trees")
        {
            filterId = "tree:",
            priority = 99999, // Put example provider at a low priority
            showDetailsOptions = ShowDetailsOptions.Inspector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.Inspector.html) | ShowDetailsOptions.Actions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.Actions.html),
            fetchItems = (context, items, provider) => FetchItems(context, provider),
            fetchThumbnail = (item, context) => AssetDatabase.GetCachedIcon[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetCachedIcon.html)(item.id) as Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html),
            fetchPreview = (item, context, size, options) => AssetDatabase.GetCachedIcon[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetCachedIcon.html)(item.id) as Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html),
            fetchLabel = (item, context) => AssetDatabase.LoadMainAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadMainAssetAtPath.html)(item.id).name,
            fetchDescription = (item, context) => AssetDatabase.LoadMainAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadMainAssetAtPath.html)(item.id).name,
            toObject = (item, type) => AssetDatabase.LoadMainAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadMainAssetAtPath.html)(item.id),
            trackSelection = TrackSelection,
            startDrag = StartDrag
        };
    }

    private static IEnumerable<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> FetchItems(SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) provider)
    {
        if (context.empty)
            yield break;

        // Yield items asynchronously which is the recommended way.
        foreach (var guid in AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("t:Prefab tree " + context.searchQuery))
            yield return provider.CreateItem(context, AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)(guid), null, null, null, null);
    }

    private static void TrackSelection(SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) searchItem, SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) searchContext)
    {
        EditorGUIUtility.PingObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.PingObject.html)(AssetDatabase.LoadMainAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadMainAssetAtPath.html)(searchItem.id));
    }

    private static void StartDrag(SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) item, SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context)
    {
        if (context.selection.Count > 1)
        {
            var selectedObjects = context.selection.Select(i => AssetDatabase.LoadMainAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadMainAssetAtPath.html)(i.id));
            var paths = context.selection.Select(i => i.id).ToArray();
            StartDrag(selectedObjects.ToArray(), paths, item.GetLabel(context, true));
        }
        else
            StartDrag(new[] { AssetDatabase.LoadMainAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadMainAssetAtPath.html)(item.id) }, new[] { item.id }, item.GetLabel(context, true));
    }

    public static void StartDrag(UnityEngine.Object[] objects, string[] paths, string label = null)
    {
        if (paths == null || paths.Length == 0)
            return;
        DragAndDrop.PrepareStartDrag[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.PrepareStartDrag.html)();
        DragAndDrop.objectReferences[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop-objectReferences.html) = objects;
        DragAndDrop.paths[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop-paths.html) = paths;
        DragAndDrop.StartDrag[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.StartDrag.html)(label);
    }


    [SearchActionsProvider]
    internal static IEnumerable<SearchAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchAction.html)> ActionHandlers()
    {
        yield return new SearchAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchAction.html)(id, "Insert tree", null, "Insert a single tree in scene", (SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) item) => InsertPrefab(item.id));
    }

    static GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) InsertPrefab(string path)
    {
        return (GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html))PrefabUtility.InstantiatePrefab[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.InstantiatePrefab.html)(
            AssetDatabase.LoadMainAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadMainAssetAtPath.html)(path),
            Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html) != null ? Selection.activeGameObject.transform : null);
    }
}

```

Another example that allows to search for lights and modify them. This provider uses another provider to get the lights.
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class LightsSearchProvider
{
    [SearchItemProvider]
    internal static SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) CreateProvider()
    {
        return new SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html)("example_lights", "Lights")
        {
            filterId = "z:",
            priority = 99999, // Put example provider at a low priority
            showDetailsOptions = ShowDetailsOptions.Inspector[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ShowDetailsOptions.Inspector.html),
            fetchItems = (context, items, provider) => FetchItems(context, provider),
            toObject = (item, type) => item.data as Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html),
            onEnable = () => { /*Cache[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cache.html) some data in here*/ },
            onDisable = () => { /*Clear the cache*/ },

            // This provider can be used in the scene view contextually.
            isEnabledForContextualSearch = () => IsFocusedWindowTypeName("SceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html)")
        };
    }

    static IEnumerable<SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html)> FetchItems(SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) provider)
    {
        if (context.empty)
            yield break;

        var sceneProvider = SearchService.GetProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.GetProvider.html)("scene");
        using (var sceneQuery = SearchService.CreateContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.CreateContext.html)(sceneProvider, $"t:light {context.searchQuery}"))
        using (var results = SearchService.Request[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.Request.html)(sceneQuery))
        {
            var lightIcon = EditorGUIUtility.FindTexture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.FindTexture.html)("Lighting");
            foreach (var r in results)
            {
                if (r == null)
                {
                    // ***IMPORTANT***: Make sure to yield so you do not block the main thread waiting for results.
                    yield return null;
                }
                else
                {
                    yield return provider.CreateItem(context, r.id,
                        r.GetLabel(sceneQuery, true), r.GetDescription(sceneQuery, true),
                        lightIcon, r.ToObject<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)>().GetComponent<Light[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Light.html)>());
                }
            }
        }
    }

    static bool IsFocusedWindowTypeName(string focusWindowName)
    {
        return EditorWindow.focusedWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-focusedWindow.html) != null && EditorWindow.focusedWindow.GetType().ToString().EndsWith("." + focusWindowName);
    }

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html)/Show lights")]
    public static void ShowLights()
    {
        // Search for directional lights (lights with "directional" in their name)
        SearchService.ShowWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.ShowWindow.html)(SearchService.CreateContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchService.CreateContext.html)("z:directional"));
    }
}

```

### Properties
Property | Description  
---|---  
[actions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-actions.html) | Search provider actions.  
[active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-active.html) | Indicates if the search provider is active or not. Inactive search providers are ignored by the search service. The active state can be toggled in the search settings.  
[fetchColumns](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-fetchColumns.html) | Handler used to enumerate search columns to be used in the Search Table view.  
[fetchDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-fetchDescription.html) | Handler to provide an asynchronous description for an item. Is called when the item is about to be displayed. Allows a plugin provider to only fetch long descriptions when they are needed.  
[fetchItems](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-fetchItems.html) | MANDATORY: Handler to get items for a given search context. The return value is an object that can be of type IEnumerable or IEnumerator. The enumeration of those objects should return SearchItems.  
[fetchLabel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-fetchLabel.html) | Handler used to fetch and format the label of a search item.  
[fetchPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-fetchPreview.html) | Similar to fetchThumbnail, fetchPreview usually returns a bigger preview. The Search UI will progressively show one preview each frame, preventing the UI from blocking if many previews need to be generated at the same time.  
[fetchPropositions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-fetchPropositions.html) | Handler used to enumerate search propositions when the user is using TAB to auto-complete a query.  
[fetchThumbnail](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-fetchThumbnail.html) | Handler to provide an asynchronous thumbnail for an item. Is called when the item is about to be displayed. Compared to preview a thumbnail should be small and returned as fast as possible. Use fetchPreview if you want to generate a preview that is bigger and slower to return. Allows a plugin provider to only fetch/generate previews when they are needed.  
[filterId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-filterId.html) | Text token used to "filter" by search provider (ex: "me:", "p:", "s:").  
[id](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-id.html) | Search provider unique ID.  
[isEnabledForContextualSearch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-isEnabledForContextualSearch.html) | Called when search is invoked in "contextual mode". Returns true if the search provider is enabled for this search context.  
[isExplicitProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-isExplicitProvider.html) | This search provider is only active when specified explicitly using the filterId.  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-name.html) | Unique ID of the search provider.  
[onDisable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-onDisable.html) | Called when the SearchWindow is closed. Allows the search provider to release cached resources.  
[onEnable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-onEnable.html) | Called when the SearchWindow is opened. Allows the search provider to perform some caching.  
[priority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-priority.html) | Hint to sort the search provider. Affects the order of search results and the order in which search providers are shown in the FilterWindow.  
[showDetails](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-showDetails.html) | Indicates if the search provider can show additional details or not.  
[showDetailsOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-showDetailsOptions.html) | Defines the details options to be shown.  
[startDrag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-startDrag.html) | If implemented, the item supports drag. It is up to the SearchProvider to properly set up the DragAndDrop manager.  
[toObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-toObject.html) | Returns any valid Unity object held by the search item.  
[trackSelection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-trackSelection.html) | Called when the selection changed and can be tracked.  
[type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-type.html) | The search provider type can be another search provider id that provider is based on. This is used when we have multiple groups in the search view that list results from a similar provider.  
### Constructors
Constructor | Description  
---|---  
[SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-ctor.html) | Create a new SearchProvider.  
### Public Methods
Method | Description  
---|---  
[CreateItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.CreateItem.html) | Helper function to create a new search item for the current search provider.  
* * *
