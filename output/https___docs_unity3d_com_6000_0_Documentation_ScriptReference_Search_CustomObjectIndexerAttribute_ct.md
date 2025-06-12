* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.CustomObjectIndexerAttribute-ctor.html

# CustomObjectIndexerAttribute Constructor
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
public CustomObjectIndexerAttribute(Type type); 
### Parameters
Parameter | Description  
---|---  
type | Type of object to be indexed.  
### Description
Register a new Indexing function bound to the specific type.
```
[CustomObjectIndexer(typeof(SceneAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneAsset.html)), version = 2 /* update me when the code below changes */)]
internal static void IndexSceneName(CustomObjectIndexerTarget[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.CustomObjectIndexerTarget.html) context, ObjectIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectIndexer.html) indexer)
{
    if (!(context.target is SceneAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneAsset.html) sceneAsset))
        return;

    indexer.IndexWordComponents(context.documentIndex, sceneAsset.name);
}

```

* * *
