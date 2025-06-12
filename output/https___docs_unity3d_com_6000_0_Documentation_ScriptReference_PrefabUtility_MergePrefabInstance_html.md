* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.MergePrefabInstance.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).MergePrefabInstance
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
public static void MergePrefabInstance([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) instanceRoot); 
### Parameters
Parameter | Description  
---|---  
instanceRoot | Root of Prefab instance to update.  
### Description
Forces a Prefab instance to merge with changes from the Prefab Asset.
Unity will in most cases handle re-merging of the Prefab instance when you make changes in the Editor or via scripting. However, as shown in the example below, there are some rare cases where editing a Prefab instance from script requires you to force merge the instance to get immediate updates.  
  
If you do not call MergePrefabInstance in those rare cases the re-merge will happen automatically at the end of the current frame, but if you need the changes reflected immediately in your script you have to force the merge.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// This example shows how to use PrefabUtility.MergePrefabInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.MergePrefabInstance.html) to force update an instance after some changes  
  
public class SuppressedComponentExample
{
    public static void MergePrefabInstanceExample()
    {
        var instance = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("MyPrefabInstance");
        const string path = "Assets/MyPrefab.prefab";
        var prefab = PrefabUtility.SaveAsPrefabAssetAndConnect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SaveAsPrefabAssetAndConnect.html)(instance, path, InteractionMode.AutomatedAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.AutomatedAction.html));  
  
        // Add Component[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) to instance
        var component = instance.AddComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();  
  
        // Add same type of component to the Prefab asset
        using (var scope = new PrefabUtility.EditPrefabContentsScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.EditPrefabContentsScope.html)(path))
        {
            scope.prefabContentsRoot.AddComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
        }  
  
        // Because a Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) already exists on the Prefab instance the one from the asset will be suppressed
        // we can get the suppressor and verify this
        var suppressor = instance.GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Is component part of the Prefab instance: {PrefabUtility.IsPartOfPrefabInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsPartOfPrefabInstance.html)(suppressor)}");  
  
        // Destroy the suppressor to make the suppressed object return to glory
        Undo.DestroyObjectImmediate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.DestroyObjectImmediate.html)(suppressor);
        PrefabUtility.MergePrefabInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.MergePrefabInstance.html)(instance);  
  
        // Now we will get the former suppressed component and verify that it is actually part of the prefab
        var formerSuppressed = instance.GetComponent<Rigidbody[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html)>();
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Is component part of the Prefab instance: {PrefabUtility.IsPartOfPrefabInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsPartOfPrefabInstance.html)(formerSuppressed)}");
    }
}

```

* * *
