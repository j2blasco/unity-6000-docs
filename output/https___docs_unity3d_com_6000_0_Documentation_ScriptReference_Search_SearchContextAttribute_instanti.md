* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContextAttribute-instantiableProviders.html

#  [SearchContextAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContextAttribute.html).instantiableProviders
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
instantiableProviders; 
### Description
Search provider concrete types that will be instantiated and assigned to the Object Picker search context.
```
[SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html)("my search", new[] { typeof(MyTextureProvider) })] public Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) mySpecialTexture2D;

class MyTextureProvider : SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html)
{
    static string ProviderId = "myTexture";

    public MyTextureProvider()
        : base(ProviderId)
    {
        fetchItems = (context, items, provider) => SearchItems(context, provider);
        fetchLabel = (item, context) =>
        {
            var assetPath = AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)((string)item.data);
            return GetNameFromPath(assetPath);
        };
        fetchThumbnail = (item, context) =>
        {
            var obj = toObject(item, typeof(Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)));
            return AssetPreview.GetAssetPreview[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetPreview.GetAssetPreview.html)(obj);
        };
        toObject = (item, type) =>
        {
            var assetPath = AssetDatabase.GUIDToAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html)((string)item.data);
            return AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)(assetPath, type);
        };
    }

    static IEnumerator SearchItems(SearchContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchContext.html) context, SearchProvider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchProvider.html) provider)
    {
        foreach (var texture2DGuid in GetMyTextures())
        {
            yield return provider.CreateItem(context, texture2DGuid, texture2DGuid.GetHashCode(), null, null, null, texture2DGuid);
        }
    }

    static IEnumerable<string> GetMyTextures()
    {
        return AssetDatabase.FindAssets[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html)("t:texture2d");
    }

    static string GetNameFromPath(string path)
    {
        var lastSep = path.LastIndexOf('/');
        if (lastSep == -1)
            return path;

        return path.Substring(lastSep + 1);
    }
}

```

* * *
