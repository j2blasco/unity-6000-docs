* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.LoadPrefabContents.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).LoadPrefabContents
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
public static [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) LoadPrefabContents(string assetPath); 
### Parameters
Parameter | Description  
---|---  
assetPath | The path of the Prefab Asset to load the contents of.  
### Returns
**GameObject** The root of the loaded contents. 
### Description
Loads a Prefab Asset at a given path into an isolated Scene and returns the root GameObject of the Prefab.
You can use this to get the content of the Prefab and modify it directly instead of going through an instance of the Prefab. This is useful for batch operations.  
  
Once you have modified the Prefab you have to write it back using [SaveAsPrefabAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SaveAsPrefabAsset.html) and then call [UnloadPrefabContents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.UnloadPrefabContents.html) to release the Prefab and isolated Scene from memory.  
  
Additional resources: [EditPrefabContentsScope](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.EditPrefabContentsScope.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Add BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html) to Prefab Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html)")]
    static void AddBoxColliderToPrefab()
    {
        // Get the Prefab Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) root GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) and its asset path.
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) assetRoot = Selection.activeObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html) as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html);
        string assetPath = AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(assetRoot);  
  
        // Load the contents of the Prefab Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html).
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) contentsRoot = PrefabUtility.LoadPrefabContents[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.LoadPrefabContents.html)(assetPath);  
  
        // Modify Prefab contents.
        contentsRoot.AddComponent<BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html)>();  
  
        // Save contents back to Prefab Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) and unload contents.
        PrefabUtility.SaveAsPrefabAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SaveAsPrefabAsset.html)(contentsRoot, assetPath);
        PrefabUtility.UnloadPrefabContents[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.UnloadPrefabContents.html)(contentsRoot);
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Add BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html) to Prefab Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html)", true)]
    static bool ValidateAddBoxColliderToPrefab()
    {
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go = Selection.activeObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html) as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html);
        if (go == null)
            return false;  
  
        return PrefabUtility.IsPartOfPrefabAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsPartOfPrefabAsset.html)(go);
    }
}

```

* * *
