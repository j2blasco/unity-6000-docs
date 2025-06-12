* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RemoveUnusedOverrides.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).RemoveUnusedOverrides
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
public static void RemoveUnusedOverrides(GameObject[] prefabInstances, [InteractionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.html) action); 
### Parameters
Parameter | Description  
---|---  
prefabInstances | List of Prefab instances to remove unused overrides from.  
action | UserAction will record undo and write result to Editor log file.  
### Description
This method identifies and removes all unused overrides from a list of Prefab Instance roots. See the manual [Unused Overides](https://docs.unity3d.com/2023.1/Documentation/Manual/UnusedOverrides.html) for more detail.
```
using System.IO;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class RemoveUnusedOverridesExample
{
    // Creates a new menu item 'Examples > Remove Unused Overrides Example' in the main menu.
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Remove Unused Overrides Example")]
    static void RemoveUnusedOverrides()
    {
        var exampleGameObject = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Example", typeof(BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html)));  
  
        // Create folder Prefabs and set the path as within the Prefabs folder,
        // and name it as the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s name with the .Prefab format
        if (!Directory.Exists[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.Exists.html)("Assets/Prefabs"))
            AssetDatabase.CreateFolder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateFolder.html)("Assets", "Prefabs");
        string localPath = "Assets/Prefabs/" + exampleGameObject.name + ".prefab";  
  
        // Make sure the file name is unique, in case an existing Prefab has the same name.
        localPath = AssetDatabase.GenerateUniqueAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GenerateUniqueAssetPath.html)(localPath);  
  
        // Create the new Prefab and log whether Prefab was saved successfully.
        var prefabAsset = PrefabUtility.SaveAsPrefabAssetAndConnect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SaveAsPrefabAssetAndConnect.html)(exampleGameObject, localPath, InteractionMode.UserAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.UserAction.html), out bool prefabSuccess);  
  
        //Set a value on the example script and record it
        exampleGameObject.GetComponent<BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html)>().center = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(2.0f, 2.0f, 2.0f);
        PrefabUtility.RecordPrefabInstancePropertyModifications[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RecordPrefabInstancePropertyModifications.html)(exampleGameObject.GetComponent<BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html)>());  
  
        //Remove the component from the prefab asset. We now have an unused override.
        PrefabUtility.ApplyRemovedComponent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.ApplyRemovedComponent.html)(exampleGameObject, prefabAsset.GetComponent(typeof(BoxCollider[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoxCollider.html))), InteractionMode.UserAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.UserAction.html));  
  
        //Remove the unused override that was created earlier
        PrefabUtility.RemoveUnusedOverrides[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RemoveUnusedOverrides.html)(new [] { exampleGameObject }, InteractionMode.UserAction[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InteractionMode.UserAction.html));
    }
}
```

* * *
