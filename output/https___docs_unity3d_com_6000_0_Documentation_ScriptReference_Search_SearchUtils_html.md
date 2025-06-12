* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.html

# SearchUtils
class in UnityEditor.Search
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
### Description
Provides various utility functions that are used by [SearchProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html).
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections;
using System.Globalization;
using System.Linq;
using UnityEditor.Search;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;

/// <summary>
/// Custom provider showing how to implement a custom Query Engine supporting a Spatial search filter.
/// </summary>
public static class SpatialProvider
{
    internal static string type = "spl";
    internal static string displayName = "Spatial";

    static GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)[] s_GameObjects;
    static QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)> s_QueryEngine;

    [SearchItemProvider]
    internal static SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) CreateProvider()
    {
        return new SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html)(type, displayName)
        {
            active = false,
            filterId = "spl:",
            onEnable = OnEnable,
            fetchItems = (context, items, provider) => SearchItems(context, provider),
            fetchLabel = FetchLabel,
            fetchDescription = FetchDescription,
            fetchThumbnail = FetchThumbnail,
            fetchPreview = FetchPreview,
            trackSelection = TrackSelection,
            isExplicitProvider = false,
        };
    }

    static void OnEnable()
    {
        s_GameObjects = SearchUtils.FetchGameObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.FetchGameObjects.html)().ToArray();
        s_QueryEngine = new QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)>();

        // Id supports all operators
        s_QueryEngine.AddFilter("id", go => go.GetInstanceID());
        // Name supports only :, = and !=
        s_QueryEngine.AddFilter("n", go => go.name, new[] {":", "=", "!="});

        // Add distance filtering. Does not support :.
        s_QueryEngine.AddFilter("dist", DistanceHandler, DistanceParamHandler, new[] {"=", "!=", "<", ">", "<=", ">="});
    }


    static IEnumerator SearchItems(SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) provider)
    {
        var query = s_QueryEngine.ParseQuery(context.searchQuery);
        if (!query.valid)
            yield break;

        var filteredObjects = query.Apply(s_GameObjects);
        foreach (var filteredObject in filteredObjects)
        {
            yield return provider.CreateItem(filteredObject.GetInstanceID().ToString(), null, null, null, filteredObject.GetInstanceID());
        }
    }


    static string FetchLabel(SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) item, SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context)
    {
        if (item.label != null)
            return item.label;

        var go = ObjectFromItem(item);
        if (!go)
            return item.id;

        var transformPath = SearchUtils.GetTransformPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetTransformPath.html)(go.transform);
        var components = go.GetComponents<Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html)>();
        if (components.Length > 2 && components[1] && components[components.Length - 1])
            item.label = $"{transformPath} ({components[1].GetType().Name}..{components[components.Length - 1].GetType().Name})";
        else if (components.Length > 1 && components[1])
            item.label = $"{transformPath} ({components[1].GetType().Name})";
        else
            item.label = $"{transformPath} ({item.id})";

        return item.label;
    }


    static string FetchDescription(SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) item, SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context)
    {
        var go = ObjectFromItem(item);
        return (item.description = SearchUtils.GetHierarchyPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetHierarchyPath.html)(go));
    }


    static Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) FetchThumbnail(SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) item, SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context)
    {
        var obj = ObjectFromItem(item);
        if (obj == null)
            return null;

        return item.thumbnail = GetThumbnailForGameObject(obj);
    }

    static Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) FetchPreview(SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) item, SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) size, FetchPreviewOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.FetchPreviewOptions.html) options)
    {
        var obj = ObjectFromItem(item);
        if (obj == null)
            return item.thumbnail;

        var assetPath = SearchUtils.GetHierarchyAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetHierarchyAssetPath.html)(obj, true);
        if (string.IsNullOrEmpty(assetPath))
            return item.thumbnail;

        if (options.HasFlag(FetchPreviewOptions.Large[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.FetchPreviewOptions.Large.html)))
        {
            if (AssetPreview.GetAssetPreview[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPreview.GetAssetPreview.html)(obj) is Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex)
                return tex;
        }
        return GetAssetPreviewFromPath(assetPath, size, options);
    }


    static void TrackSelection(SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) item, SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context)
    {
        var obj = ObjectFromItem(item);
        if (obj)
            Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html) = obj;
        if (SceneView.lastActiveSceneView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-lastActiveSceneView.html) != null)
            SceneView.lastActiveSceneView.FrameSelected();
    }

    static float DistanceHandler(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go, Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) p)
    {
        return (go.transform.position - p).magnitude;
    }

    static Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) DistanceParamHandler(string param)
    {
        if (param == "selection")
        {
            var centerPoint = Selection.gameObjects.Select(go => go.transform.position).Aggregate((v1, v2) => v1 + v2);
            centerPoint /= Selection.gameObjects.Length;
            return centerPoint;
        }

        if (param.StartsWith("[") && param.EndsWith("]"))
        {
            param = param.Trim('[', ']');
            var vectorTokens = param.Split(',');
            var vectorValues = vectorTokens.Select(token => float.Parse(token, CultureInfo.InvariantCulture.NumberFormat)).ToList();
            while (vectorValues.Count < 3)
                vectorValues.Add(0f);
            return new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(vectorValues[0], vectorValues[1], vectorValues[2]);
        }

        var obj = s_GameObjects.FirstOrDefault(go => go.name == param);
        if (!obj)
            return Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);
        return obj.transform.position;
    }

    static GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) ObjectFromItem(SearchItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchItem.html) item)
    {
        var instanceID = Convert.ToInt32(item.id);
        var obj = EditorUtility.InstanceIDToObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.InstanceIDToObject.html)(instanceID) as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html);
        return obj;
    }

    static Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) GetThumbnailForGameObject(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go)
    {
        var thumbnail = PrefabUtility.GetIconForGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetIconForGameObject.html)(go);
        if (thumbnail)
            return thumbnail;
        return EditorGUIUtility.ObjectContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility.ObjectContent.html)(go, go.GetType()).image as Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html);
    }

    static Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) GetAssetPreviewFromPath(string path, Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) previewSize, FetchPreviewOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.FetchPreviewOptions.html) previewOptions)
    {
        var obj = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<UnityEngine.Object>(path);
        if (obj == null)
            return null;
        var preview = AssetPreview.GetAssetPreview[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPreview.GetAssetPreview.html)(obj);
        if (preview == null || previewOptions.HasFlag(FetchPreviewOptions.Large[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.FetchPreviewOptions.Large.html)))
        {
            var largePreview = AssetPreview.GetMiniThumbnail[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPreview.GetMiniThumbnail.html)(obj);
            if (preview == null || (largePreview != null && largePreview.width > preview.width))
                preview = largePreview;
        }
        return preview;
    }
}

```

### Static Properties
Property | Description  
---|---  
[entrySeparators](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils-entrySeparators.html) | Separators used to split an entry into indexable tokens.  
### Static Methods
Method | Description  
---|---  
[CreateGroupProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.CreateGroupProvider.html) | Copy of a search provider to create a new group copy.  
[CreateQuery](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.CreateQuery.html) | Creates a new search query.  
[CreateSceneResult](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.CreateSceneResult.html) | Creates a search item compatible with the scene provider.  
[EnumerateAllQueries](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.EnumerateAllQueries.html) | Enumerate all user and project search queries.  
[FetchGameObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.FetchGameObjects.html) | Utility function to fetch all the game objects in a particular scene.  
[FindQuery](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.FindQuery.html) | Find a given search query given its GUID.  
[FindShiftLeftVariations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.FindShiftLeftVariations.html) | Extract all variations on a word. As an example: the word hello would have the following variations: h, he, hel, hell, hello.  
[FormatBytes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.FormatBytes.html) | Formats a number into a file size in bytes string.  
[FormatCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.FormatCount.html) | Formats a number into a shorten number string.  
[FrameAssetFromPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.FrameAssetFromPath.html) | Ping an asset in the project browser.  
[GetAssetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetAssetPath.html) | Returns the asset path of a search item if any.  
[GetAssetPreviewFromPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetAssetPreviewFromPath.html) | Returns a preview texture to be used in the search view.  
[GetAssetThumbnailFromPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetAssetThumbnailFromPath.html) | Returns a thumbnail texture to be used in the search view.  
[GetHierarchyAssetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetHierarchyAssetPath.html) | Get the path of the scene (or prefab) containing a GameObject.  
[GetHierarchyPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetHierarchyPath.html) | Get the hierarchy path of a GameObject including the scene name if includeScene is set to true.  
[GetMainAssetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetMainAssetInstanceID.html) | Returns an asset instance ID.  
[GetMainWindowCenteredPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetMainWindowCenteredPosition.html) | Returns a UnityEngine.Rect to center a window on the main Unity Editor window.  
[GetObjectPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetObjectPath.html) | Get the path of a Unity Object. If it is a GameObject or a Component it is the . Else it is the asset name.  
[GetSceneObjectPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetSceneObjectPreview.html) | Returns a scene object preview to be used in the search view.  
[GetTransformPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetTransformPath.html) | Format the pretty name of a Transform component by appending all the parent hierarchy names.  
[GetTypeIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetTypeIcon.html) | Returns a thumbnail for a given type that can be displayed in a search view. See SearchProvider.fetchThumbnail.  
[MatchSearchGroups](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.MatchSearchGroups.html) | Helper function to match a string against the SearchContext. This will try to match the search query against each token of content (similar to the AddComponent menu workflow).  
[OpenQuery](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.OpenQuery.html) | Open a search view for a given query.  
[PingAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.PingAsset.html) | Ping an object.  
[SelectMultipleItems](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.SelectMultipleItems.html) | Select and ping multiple objects in the Project Browser.  
[ShowColumnSelector](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.ShowColumnSelector.html) | Opens an auxiliary column selector window to allow the user to search for a column to be added.  
[ShowIconPicker](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.ShowIconPicker.html) | Opens a search picker to select an icon.  
[SplitCamelCase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.SplitCamelCase.html) | Tokenize a string each capital letter.  
[SplitEntryComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.SplitEntryComponents.html) | Split an entry according to a specified list of separators.  
[SplitFileEntryComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.SplitFileEntryComponents.html) | Split a file entry according to a list of separators and find all the variations on the entry name.  
[StartDrag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.StartDrag.html) | Utility function used to initiate a drag operation from a search view.  
[TryParse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.TryParse.html) | Try to parse an expression into a number.  
* * *
