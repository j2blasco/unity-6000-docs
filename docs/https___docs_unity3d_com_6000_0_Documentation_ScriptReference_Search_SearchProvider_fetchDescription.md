* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-fetchDescription.html

#  [SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html).fetchDescription
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
fetchDescription; 
### Description
Handler to provide an asynchronous description for an item. Is called when the item is about to be displayed. Allows a plugin provider to only fetch long descriptions when they are needed.
```
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

```

* * *
