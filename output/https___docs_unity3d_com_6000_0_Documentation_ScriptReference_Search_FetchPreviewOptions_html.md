* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.FetchPreviewOptions.html

# FetchPreviewOptions
enumeration
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
Options for the search provider on how the preview should be fetched.
These options are used by the [SearchProvider.fetchPreview](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider-fetchPreview.html) functor.
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
### Properties
Property | Description  
---|---  
[None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.FetchPreviewOptions.None.html) | No options are defined.  
[Preview2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.FetchPreviewOptions.Preview2D.html) | Indicates that the search provider should generate a 2D preview.  
[Preview3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.FetchPreviewOptions.Preview3D.html) | Indicates that the search provider should generate a 3D preview.  
[Normal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.FetchPreviewOptions.Normal.html) | Indicates that the preview size should be around 128x128.  
[Large](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.FetchPreviewOptions.Large.html) | Indicates that the preview resolution should be higher than 256x256.  
* * *
