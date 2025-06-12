* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RevertRemovedGameObject.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).RevertRemovedGameObject
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
public static void RevertRemovedGameObject([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObjectInInstance, [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) assetGameObject, [InteractionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.html) action); 
### Parameters
Parameter | Description  
---|---  
gameObjectInInstance | A GameObject in the Prefab instance containing the removed GameObject.  
assetGameObject | The GameObject on the Prefab Asset corresponding to the removed GameObject on the instance.  
action | The interaction mode for this action.  
### Description
Adds this removed GameObject back on the Prefab instance.
After the revert action the GameObject will once again exist on the Prefab instance.  
  
The GameObject's components and children will also exist again, unless they had previously been removed.  
  
Note that added GameObjects and added component overrides, which were in the hierarchy of the reverted GameObject before it was removed, will not be restored.  
  
Additional resources: [PrefabUtility.ApplyRemovedGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyRemovedGameObject.html), [PrefabUtility.GetRemovedGameObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetRemovedGameObjects.html).
```
using System.Collections.Generic;
using System.IO;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.SceneManagement;
using UnityEngine;  
  
// Creates new menu items under 'Examples' in the main menu.
public class RevertRemovedGameObjectExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/RevertRemovedGameObject Example 1")]
    static void CreatePrefabAndRevertChanges()
    {
        // Create folder Prefabs and set the path as within the Prefabs folder,
        // and name it as the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s name with the .Prefab format
        if (!Directory.Exists[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.Exists.html)("Assets/Prefabs"))
            AssetDatabase.CreateFolder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateFolder.html)("Assets", "Prefabs");  
  
        //Setup hierarchy with root and one child
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) rootGameObject = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Root");
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) child = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Child");
        child.transform.parent = rootGameObject.transform;  
  
        //Create prefab based on the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) hierarchy we just created
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefabAsset = PrefabUtility.SaveAsPrefabAssetAndConnect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SaveAsPrefabAssetAndConnect.html)(rootGameObject, "Assets/Prefabs/" + rootGameObject.name + ".prefab", InteractionMode.AutomatedAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.AutomatedAction.html));  
  
        //Get the corresponding object matching the Child GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) that was destroyed
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) correspondingChildGameObject = prefabAsset.transform.GetChild(0).gameObject;  
  
        //Destroy child GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) so we can apply the override to the Prefab
        Object.DestroyImmediate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html)(child);  
  
        //Use the variables from above to revert the removed GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) override in the instance and restore the child GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        PrefabUtility.RevertRemovedGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RevertRemovedGameObject.html)(rootGameObject, correspondingChildGameObject, InteractionMode.AutomatedAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.AutomatedAction.html));  
  
        if (prefabAsset.transform.childCount == 1)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("'Child' GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) was removed and the override reverted successfully.");
        else
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The override was not reverted successfully");
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/RevertRemovedGameObject Example 2")]
    static void CreatePrefabAndApplyChangesWithGetRemovedGameObjects()
    {
        // Create folder Prefabs and set the path as within the Prefabs folder,
        // and name it as the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s name with the .Prefab format
        if (!Directory.Exists[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.Exists.html)("Assets/Prefabs"))
            AssetDatabase.CreateFolder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateFolder.html)("Assets", "Prefabs");  
  
        //Setup hierarchy with root and one child
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) rootGameObject = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Root");
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) child = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Child");
        child.transform.parent = rootGameObject.transform;  
  
        //Create prefab based on the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) hierarchy we just created
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefabAsset = PrefabUtility.SaveAsPrefabAssetAndConnect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SaveAsPrefabAssetAndConnect.html)(rootGameObject, "Assets/Prefabs/" + rootGameObject.name + ".prefab", InteractionMode.AutomatedAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.AutomatedAction.html));  
  
        //Destroy child GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) so we can apply the override to the Prefab
        Object.DestroyImmediate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html)(child);  
  
        //Get the override and the information to apply the changes to the Prefab asset
        List<RemovedGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.RemovedGameObject.html)> removedGameObjects = PrefabUtility.GetRemovedGameObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetRemovedGameObjects.html)(rootGameObject);
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) assetGameObject = removedGameObjects[0].assetGameObject;
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) parentOfRemovedGameObjectInInstance = removedGameObjects[0].parentOfRemovedGameObjectInInstance;  
  
        //Use the variables from above to revert the removed GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) override in the instance and restore the child GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        PrefabUtility.RevertRemovedGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RevertRemovedGameObject.html)(parentOfRemovedGameObjectInInstance, assetGameObject, InteractionMode.AutomatedAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.AutomatedAction.html));  
  
        if (prefabAsset.transform.childCount == 1)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("'Child' GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) was removed and the override reverted successfully.");
        else
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The override was not reverted successfully");
    }
}

```

* * *
