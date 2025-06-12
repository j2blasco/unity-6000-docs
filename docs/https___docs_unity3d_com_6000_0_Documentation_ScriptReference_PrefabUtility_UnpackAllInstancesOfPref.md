* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.UnpackAllInstancesOfPrefab.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).UnpackAllInstancesOfPrefab
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
public static void UnpackAllInstancesOfPrefab([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefabRoot, [PrefabUnpackMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUnpackMode.html) unpackMode, [InteractionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.html) action); 
### Parameters
Parameter | Description  
---|---  
prefabRoot | The root GameObject of a Prefab Asset used to find all Prefab instances in open scenes that should be unpacked.  
unpackMode | Whether to unpack the outermost root or unpack completely.  
action | The interaction mode to use for this action.  
### Description
Unpacks all instances of a given Prefab Asset root GameObject in all open scenes so that all instances are replaced with the contents of the Prefab Asset while retaining all override values.
The Prefab instances will not be unpacked in closed scenes. This function uses [PrefabUtility.FindAllInstancesOfPrefab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.FindAllInstancesOfPrefab.html) to determine which instances to unpack and calls [PrefabUtility.UnpackPrefabInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.UnpackPrefabInstance.html) for each instance.  
  
Unpacking throws an ArgumentException if the given object is not the root GameObject of a Prefab Asset.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class Example
{
    public static void UnpackAllInstancesOfPrefab(string prefabPath)
    {
        var prefabAssetRoot = AssetDatabase.LoadMainAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadMainAssetAtPath.html)(prefabPath) as GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html);
        if (prefabAssetRoot != null)
        {
            PrefabUtility.UnpackAllInstancesOfPrefab[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.UnpackAllInstancesOfPrefab.html)(prefabAssetRoot, PrefabUnpackMode.OutermostRoot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUnpackMode.OutermostRoot.html), InteractionMode.UserAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.UserAction.html));
        }
    }
}

```

* * *
