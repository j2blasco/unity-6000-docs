* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.GetHierarchyAssetPath.html

#  [SearchUtils](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchUtils.html).GetHierarchyAssetPath
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
## Declaration
public static string GetHierarchyAssetPath([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject, bool prefabOnly); 
### Parameters
Parameter | Description  
---|---  
gameObject | GameObject to find the scene path.  
prefabOnly | If true, will return a path only if the GameObject is a prefab.  
### Returns
**string** Returns the path of a scene or prefab. 
### Description
Get the path of the scene (or prefab) containing a GameObject.
```
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

```

* * *
