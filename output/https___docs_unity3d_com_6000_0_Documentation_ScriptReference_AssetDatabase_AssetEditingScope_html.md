* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AssetEditingScope.html

# AssetEditingScope
class in UnityEditor
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
Places the Asset Database into a state that temporarily prevents automatic import, allowing you to group several asset imports together into one larger import.
This class allows you to pause the Asset Database's automatic import of new or modified assets. This is useful if you want to perform actions via script that make multiple changes to assets without the Asset Database importing each change in a separate import process.   
  
Instead, you can pause imports, make multiple changes, then resume imports, which means Unity will only perform one input process for all the changes you made while the importing was paused.  
  
This class is an alternative to the [AssetDatabase.StartAssetEditing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.StartAssetEditing.html) and [AssetDatabase.StopAssetEditing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.StopAssetEditing.html) methods, which serve the same purpose.  
  
The `AssetEditingScope` class is intended to be used within a `using` statement, which automatically disposes of the class, as in the following example:
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class AssetEditingScopeExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("APIExamples/AssetEditingScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AssetEditingScope.html)")]
    static void CallAssetDatabaseAPIsBetweenAssetEditingScope()
    {
        // Place the Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) Database in a state where
        // importing is suspended for most APIs
        using (var editingScope = new AssetDatabase.AssetEditingScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AssetEditingScope.html)())
        {
            // Modify the assets however we like
            AssetDatabase.CopyAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CopyAsset.html)("Assets/CopyAsset.txt", "Assets/Text/CopyAsset.txt");
            AssetDatabase.MoveAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.MoveAsset.html)("Assets/MoveAsset.txt", "Assets/Text/MoveAsset.txt");
        }
        // Assets will now be imported again, as editingScope has been disposed.
    }
}

```

If you use it in a different context other than a `using` statement, you must ensure that its `Dispose()` method is called or the Asset Database will remain in a paused state.  
  
Additional resources: [AssetDatabase.StartAssetEditing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.StartAssetEditing.html), [AssetDatabase.StopAssetEditing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.StopAssetEditing.html).
### Constructors
Constructor | Description  
---|---  
[AssetDatabase.AssetEditingScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AssetEditingScope-ctor.html) | Instantiates AssetEditingScope. Equivalent to calling AssetDatabase.StartAssetEditing().  
### Public Methods
Method | Description  
---|---  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AssetEditingScope.Dispose.html) | Disposes of AssetEditingScope. Equivalent to calling AssetDatabase.StopAssetEditing().  
* * *
