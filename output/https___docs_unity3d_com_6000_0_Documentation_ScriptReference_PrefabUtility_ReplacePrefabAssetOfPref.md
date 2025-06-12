* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ReplacePrefabAssetOfPrefabInstance.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).ReplacePrefabAssetOfPrefabInstance
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
public static void ReplacePrefabAssetOfPrefabInstance([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefabInstanceRoot, [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefabAssetRoot, [InteractionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.html) mode); 
## Declaration
public static void ReplacePrefabAssetOfPrefabInstance([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefabInstanceRoot, [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefabAssetRoot, [PrefabReplacingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabReplacingSettings.html) settings, [InteractionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.html) mode); 
### Parameters
Parameter | Description  
---|---  
prefabInstanceRoot | The Prefab instance root that will have its Prefab Asset replaced.  
prefabAssetRoot | The new Prefab Asset used for the Prefab instance.  
mode | The interaction mode used.  
settings | The settings used to control the details of the replacement.  
### Description
Replace the Prefab Asset for a Prefab instance that exists in a Scene or for a nested Prefab instance inside another Prefab.
This function will keep the Prefab instance root position, rotation and scale in the Scene but merge the contents from the new Prefab Asset while, by default, maintaining as many overrides and references as possible by using name based matching. Note that the root GameObject and its components will always reuse these objects regardless of the [ObjectMatchMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectMatchMode.html), so references to these objects will always survive a replacement. Use [ObjectMatchMode.ByHierarchy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectMatchMode.ByHierarchy.html) which will retain references if GameObjects and Components are matched up using their full GameObject hierarchy path so ensure all siblings have unique names. When using [ObjectMatchMode.ByName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectMatchMode.ByName.html) an object match is only performed if the name match is unique. It is therefore recommended that the Prefab instance and Prefab Asset only have unique names in the hierarchy of GameObjects. Matching cannot be done for GameObjects with duplicate names.  
  
No property overrides are deleted from the serialized state of the Prefab instance so replacing back and forth between different Prefab Assets is a non-destructive action for property overrides. When the final Prefab instance is decided upon then any unused overrides can be cleaned up from either Hierarchy or Overrides window. Added Components are preserved if a name match exists, otherwise the added Component is deleted. Added GameObjects are preserved by adding them to the root of the new instance if no name match was found for its parent GameObject. Since an added GameObject can have a full hierarchy under it, we leave it to you to decide whether it makes sense to delete the object if it proves redundant on the new instance. This can be done from either the Hierarchy or Overrides window. For explict control over which overrides should be cleared use the [PrefabReplacingSettings.prefabOverridesOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabReplacingSettings-prefabOverridesOptions.html) flags found in the [PrefabReplacingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabReplacingSettings.html).  
  
Additional resources: [ReplacePrefabAssetOfPrefabInstances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ReplacePrefabAssetOfPrefabInstances.html), [ConvertToPrefabInstance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ConvertToPrefabInstance.html).
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
class PrefabReplacing
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Assets/Replace Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) Selection[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html) with Prefab Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html)", false, 32)]
    static void ReplaceSelectedWithPrefabInstance(MenuCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuCommand.html) menuCommand)
    {
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefabAsset = null;
        var listOfInstanceRoots = new List<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)>();
        var listOfPlainGameObjects = new List<GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)>();
        foreach (var go in Selection.gameObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-gameObjects.html))
        {
            if (AssetDatabase.Contains[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.Contains.html)(go))
                prefabAsset = go;
            else if (PrefabUtility.IsOutermostPrefabInstanceRoot[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsOutermostPrefabInstanceRoot.html)(go))
                listOfInstanceRoots.Add(go);
            else if (!PrefabUtility.IsPartOfNonAssetPrefabInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.IsPartOfNonAssetPrefabInstance.html)(go))
                listOfPlainGameObjects.Add(go);
        }  
  
        if (prefabAsset == null || (listOfInstanceRoots.Count == 0 && listOfPlainGameObjects.Count == 0))
        {
            ShowHelpDialog(prefabAsset);
            return;
        }  
  
        if (listOfInstanceRoots.Count > 0)
        {
            var settings = new PrefabReplacingSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabReplacingSettings.html)
            {
                logInfo = true,
                objectMatchMode = ObjectMatchMode.ByHierarchy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectMatchMode.ByHierarchy.html),
                prefabOverridesOptions = PrefabOverridesOptions.ClearAllNonDefaultOverrides[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabOverridesOptions.ClearAllNonDefaultOverrides.html)
            };
            PrefabUtility.ReplacePrefabAssetOfPrefabInstances[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ReplacePrefabAssetOfPrefabInstances.html)(listOfInstanceRoots.ToArray(), prefabAsset, settings, InteractionMode.UserAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.UserAction.html));
        }  
  
        if (listOfPlainGameObjects.Count > 0)
        {
            var settings = new ConvertToPrefabInstanceSettings[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConvertToPrefabInstanceSettings.html)
            {
                logInfo = true,
                objectMatchMode = ObjectMatchMode.ByHierarchy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ObjectMatchMode.ByHierarchy.html),
            };
            PrefabUtility.ConvertToPrefabInstances[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ConvertToPrefabInstances.html)(listOfPlainGameObjects.ToArray(), prefabAsset, settings, InteractionMode.UserAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.UserAction.html));
        }
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Assets/Replace Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) Selection[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html) with Prefab Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html)", true, 32)]
    static bool ValidateReplaceSelectedWithPrefabInstance(MenuCommand[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuCommand.html) menuCommand)
    {
        foreach (var go in Selection.gameObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-gameObjects.html))
        {
            if (AssetDatabase.Contains[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.Contains.html)(go))
                return true;
        }  
  
        return false;
    }  
  
    static void ShowHelpDialog(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefabAsset)
    {
        var helptext = "Please make a multiselection with at least one Prefab instance root or plain GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) and one Prefab Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) from the Project Browser. \n\nUse Ctrl/Cmd + Click.";
        EditorUtility.DisplayDialog[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.DisplayDialog.html)("Replace Prefab Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) of Prefab instance", (prefabAsset == null ? "Prefab Asset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Asset.html) missing.\n\n" : "Prefab instance missing.\n\n") + helptext, "OK");
    }
}

```

* * *
