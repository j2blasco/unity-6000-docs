* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SaveAsPrefabAsset.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).SaveAsPrefabAsset
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
public static [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) SaveAsPrefabAsset([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) instanceRoot, string assetPath); 
## Declaration
public static [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) SaveAsPrefabAsset([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) instanceRoot, string assetPath, out bool success); 
### Parameters
Parameter | Description  
---|---  
instanceRoot | The GameObject to save as a Prefab Asset.  
assetPath | The path to save the Prefab at.  
success | The result of the save action, either successful or unsuccessful. Use this together with the console log to get more insight into the save process.  
### Returns
**GameObject** The root GameObject of the saved Prefab Asset, if available. 
### Description
Creates a Prefab Asset at the given path from the given GameObject, including any childen in the Scene without modifying the input objects.
In case some of the children are Prefab instances they will automatically become nested inside the new Prefab Asset.  
  
The input object must be a plain GameObject or the outermost root of a Prefab Instance. It cannot be a child inside a Prefab instance.  
  
If the input object is a Prefab instance root the resulting Prefab will be a Prefab Variant. If you want to create a new unique Prefab instead, you need to unpack the Prefab instance first.  
  
The returned object is the root GameObject of the saved Prefab Asset, if available. If the Editor is currently in the middle of an asset editing batch operation, as controlled with [AssetDatabase.StartAssetEditing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.StartAssetEditing.html) and [AssetDatabase.StopAssetEditing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.StopAssetEditing.html), assets are not immediately imported upon being saved. In this case, SaveAsPrefabAsset will return null even if the save was successful because the saved Prefab Asset was not yet reimported and thus not yet available.  
  
If you are saving over an existing Prefab, Unity tries to preserve references to the Prefab itself and the individual parts of the Prefab such as child GameObjects and Components. To do this, it matches the names of GameObjects between the new saved Prefab and the existing Prefab.  
  
Note: Because this matching is done by name only, if there are multiple GameObjects with the same name in the Prefab's hierarchy, you cannot predict which will be matched. Therefore if you need to ensure your references are preserved when saving over an existing prefab, you must ensure all GameObjects within the Prefab have unique names.  
  
Also note: You may encounter a similar problem in the case of preserving references to existing Components when you save over an existing Prefab, if a single GameObject within the Prefab has more than one of the same Component type attached. In this case you cannot predict which of them will be matched to the existing references.  
  
Additional resources: [PrefabUtility.SaveAsPrefabAssetAndConnect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SaveAsPrefabAssetAndConnect.html) and [Unpacking Prefab instances](https://docs.unity3d.com/6000.0/Documentation/Manual/UnpackingPrefabInstances.html).
```
// This script creates a new menu item Examples>Create Prefab in the main menu.
// Use it to create Prefab(s) from the selected GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)(s).
// Prefab(s) are placed in the "Prefabs" folder.
using System.IO;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example
{
    // Creates a new menu item 'Examples > Create Prefab' in the main menu.
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Create Prefab")]
    static void CreatePrefab()
    {
        // Keep track of the currently selected GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)(s)
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)[] objectArray = Selection.gameObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-gameObjects.html);  
  
        // Loop through every GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in the array above
        foreach (GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject in objectArray)
        {
            // Create folder Prefabs and set the path as within the Prefabs folder,
            // and name it as the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)'s name with the .Prefab format
            if (!Directory.Exists[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.Exists.html)("Assets/Prefabs"))
                AssetDatabase.CreateFolder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateFolder.html)("Assets", "Prefabs");
            string localPath = "Assets/Prefabs/" + gameObject.name + ".prefab";  
  
            // Make sure the file name is unique, in case an existing Prefab has the same name.
            localPath = AssetDatabase.GenerateUniqueAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GenerateUniqueAssetPath.html)(localPath);  
  
            // Create the new Prefab and log whether Prefab was saved successfully.
            bool prefabSuccess;
            PrefabUtility.SaveAsPrefabAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SaveAsPrefabAsset.html)(gameObject, localPath, out prefabSuccess);
            if (prefabSuccess == true)
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Prefab was saved successfully");
            else
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Prefab failed to save" + prefabSuccess);
        }
    }  
  
    // Disable the menu item if no selection is in place.
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Create Prefab", true)]
    static bool ValidateCreatePrefab()
    {
        return Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html) != null && !EditorUtility.IsPersistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.IsPersistent.html)(Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html));
    }
}

```

* * *
