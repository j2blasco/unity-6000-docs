* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectIndexer.IndexProperty.html

#  [ObjectIndexer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectIndexer.html).IndexProperty
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
public void IndexProperty(int documentIndex, string name, string value, bool saveKeyword, bool exact); 
### Parameters
Parameter | Description  
---|---  
documentIndex | Document where the indexed word was found.  
name | Key used to retrieve the value.  
value | Value to add to the index.  
saveKeyword | Define if we store this key in the keyword registry of the index.  
exact | If exact is true, only the exact match of the value will be stored in the index (not the variations).  
### Description
Adds a property value to the index. A property is specified with a key and a string value. The value will be stored with multiple variations.
The following example indexes a new boolean property named `testismobilefriendly` that will be used to search textures that match `testismobilefriendly=true` or `testismobilefriendly=false`.
```
[CustomObjectIndexer(typeof(Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)))]
static void IndexMobileFriendlyTexture(CustomObjectIndexerTarget[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.CustomObjectIndexerTarget.html) target, ObjectIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectIndexer.html) indexer)
{
    var texture = target.target as Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html);
    if (texture == null)
        return;

    bool isMobileFriendly = texture.width < 64 && texture.height < 64;
    indexer.IndexProperty(target.documentIndex, "testismobilefriendly", isMobileFriendly.ToString(), true);
}

[CustomObjectIndexer(typeof(Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)))]
static void CrashingIndexer(CustomObjectIndexerTarget[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.CustomObjectIndexerTarget.html) target, ObjectIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectIndexer.html) indexer)
{
    if (enableCrashingIndexer)
        throw new System.Exception("Crash");
}

```

See [SearchIndexer.AddProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.SearchIndexer.AddProperty.html) for more information and examples about indexing properties.
* * *
