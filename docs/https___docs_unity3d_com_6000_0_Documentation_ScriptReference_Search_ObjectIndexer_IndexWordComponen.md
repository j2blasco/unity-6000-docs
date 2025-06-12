* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectIndexer.IndexWordComponents.html

#  [ObjectIndexer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectIndexer.html).IndexWordComponents
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
public void IndexWordComponents(int documentIndex, ref string word); 
### Parameters
Parameter | Description  
---|---  
documentIndex | Document where the indexed word was found.  
word | Word to add to the index.  
### Description
Splits a word into multiple variations.
See [IndexPropertyComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectIndexer.IndexPropertyComponents.html) for some examples on how a value can be split into multiple variations. [IndexWordComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectIndexer.IndexWordComponents.html) performs the same task for words.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;

static class Example_ObjectIndexer_IndexWordComponents
{
    [CustomObjectIndexer(typeof(SceneAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneAsset.html)), version = 2 /* update me when the code below changes */)]
    internal static void IndexSceneName(CustomObjectIndexerTarget[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.CustomObjectIndexerTarget.html) context, ObjectIndexer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.ObjectIndexer.html) indexer)
    {
        if (!(context.target is SceneAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneAsset.html) sceneAsset))
            return;

        indexer.IndexWordComponents(context.documentIndex, sceneAsset.name);
    }

}

```

* * *
