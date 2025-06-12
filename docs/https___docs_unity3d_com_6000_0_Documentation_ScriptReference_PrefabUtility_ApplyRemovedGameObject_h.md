* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyRemovedGameObject.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).ApplyRemovedGameObject
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
public static void ApplyRemovedGameObject([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObjectInInstance, [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) assetGameObject, [InteractionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.html) action); 
### Parameters
Parameter | Description  
---|---  
gameObjectInInstance | A GameObject in the Prefab instance containing the removed GameObject.  
assetGameObject | The GameObject in the Prefab Asset corresponding to the removed GameObject on the instance.  
action | The interaction mode for this action.  
### Description
Removes the GameObject from the source Prefab Asset.
When a GameObject is removed from a Prefab instance, that modification is a type of [Instance Override](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabInstanceOverrides.html). The act of applying the change (the removal of the GameObject) to the Prefab means the GameObject is removed from the Prefab Asset itself, along with its components and GameObject children, and is no longer an override on the Prefab instance.  
  
When applying a removed GameObject to a Prefab Asset, you must supply the asset path as a parameter. This is because there are some situations where there are multiple possible targets to apply the change to. For example, if the GameObject was removed from a GameObject that is part of a [nested Prefab](https://docs.unity3d.com/6000.0/Documentation/Manual/NestedPrefabs.html) instance, you may have the choice of applying the change to the inner nested Prefab Asset, or to the outer root Prefab Asset. Therefore, by specifying the asset path, you make it clear to Unity which Prefab Asset the change must be applied to. It mirrors the functionality in the editor, described in [the user manual here](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabOverridesMultiLevel.html).  
  
You can read more in the user manual about the [choice of apply targets](https://docs.unity3d.com/6000.0/Documentation/Manual/PrefabOverridesMultiLevel.html).  
  
Additional resources: [PrefabUtility.ApplyAddedComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyAddedComponent.html), [PrefabUtility.ApplyAddedGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyAddedGameObject.html), [PrefabUtility.ApplyObjectOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyObjectOverride.html), [PrefabUtility.ApplyPrefabInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyPrefabInstance.html), [PrefabUtility.ApplyPropertyOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyPropertyOverride.html), [PrefabUtility.ApplyRemovedComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyRemovedComponent.html).
```
using System.Collections.Generic;
using System.IO;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.SceneManagement;
using UnityEngine;  
  
// Creates new menu items under 'Examples' in the main menu.
public class ApplyRemovedGameObjectExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/ApplyRemovedGameObject Example 1")]
    static void CreatePrefabAndApplyChanges()
    {
        //Ensure the existence of a Prefabs folder inside the Assets folder
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
  
        //Use the variables from above to apply the removed GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) override to the Prefab asset
        PrefabUtility.ApplyRemovedGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyRemovedGameObject.html)(rootGameObject, correspondingChildGameObject, InteractionMode.AutomatedAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.AutomatedAction.html));  
  
        if (prefabAsset.transform.childCount == 0)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("'Child' GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) was removed and the override was applied to the Prefab successfully.");
        else
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The override was not applied successfully");
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/ApplyRemovedGameObject Example 2")]
    static void CreatePrefabAndApplyChangesWithGetRemovedGameObjects()
    {
        //Ensure the existence of a Prefabs folder inside the Assets folder
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
  
        //Use the variables from above to apply the removed GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) override to the Prefab
        PrefabUtility.ApplyRemovedGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyRemovedGameObject.html)(parentOfRemovedGameObjectInInstance, assetGameObject, InteractionMode.AutomatedAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.AutomatedAction.html));  
  
        if (prefabAsset.transform.childCount == 0)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("'Child' GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) was removed and the override was applied to the Prefab successfully.");
        else
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("The override was not applied successfully");
    }
}

```

* * *
