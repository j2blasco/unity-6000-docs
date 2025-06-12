* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.DontSave.html

#  [HideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.html).DontSave
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
The object will not be saved to the Scene. **It will not be destroyed when a new Scene is loaded**. It is a shortcut for HideFlags.DontSaveInBuild | HideFlags.DontSaveInEditor | HideFlags.DontUnloadUnusedAsset.
You must manually clear the object from memory using DestroyImmediate to avoid memory leaks.  
  
For Prefab instances in a scene, you can set the hideflag on the Prefab instance handle object as a way to set the same hideflags on all the objects of the Prefab instance. (See [PrefabUtility.GetPrefabInstanceHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.GetPrefabInstanceHandle.html)).
```
using System.IO;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.SceneManagement;
using UnityEngine;  
  
// Creates new menu items under 'Examples' in the main menu.
public class DontSaveExamples
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) (and child) HideFlags.DontSave[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.DontSave.html) example")]
    static void DontSaveExample_RootWithDontSave()
    {
        //Setup hierarchy with root and one child
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) rootGameObject = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Root");
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) child = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Child");
        child.transform.parent = rootGameObject.transform;  
  
        rootGameObject.hideFlags = HideFlags.DontSave[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.DontSave.html);
        //child.hideFlags = HideFlags.DontSave[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.DontSave.html); //No difference for plain GameObjects as the root is marked with DontSave  
  
        //Load new scene
        EditorSceneManager.NewScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.NewScene.html)(NewSceneSetup.EmptyScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.NewSceneSetup.EmptyScene.html), NewSceneMode.Single[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.NewSceneMode.Single.html));  
  
        //Both objects still exist as the root is marked with DontSave
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Root name: " + rootGameObject.name + ", Child name: " + child.name);  
  
        //Remember to clean up, this also deleted the child GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)
        Object.DestroyImmediate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html)(rootGameObject);
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Save Prefab with child HideFlags.DontSave[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.DontSave.html) example")]
    static void DontSaveExample_Prefab_ChildNotSavedToDisk()
    {
        //Ensure the existence of a Prefabs folder inside the Assets folder
        if (!Directory.Exists[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.Directory.Exists.html)("Assets/Prefabs"))
            AssetDatabase.CreateFolder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateFolder.html)("Assets", "Prefabs");  
  
        //Setup hierarchy with root and one child
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) rootGameObject = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Root");
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) child = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Child");
        child.transform.parent = rootGameObject.transform;  
  
        //Mark child to prevent saving it
        child.hideFlags = HideFlags.DontSave[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.DontSave.html);  
  
        //Save the Prefab asset
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) prefabAsset = PrefabUtility.SaveAsPrefabAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.SaveAsPrefabAsset.html)(rootGameObject, "Assets/Prefabs/Root.prefab");  
  
        //No children in prefab as the child was marked as DontSave. The childCount is 0.
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Child GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in Prefab: " + prefabAsset.transform.childCount);  
  
        //Child still exists in scene. The childCount is 1.
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Child GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html): " + rootGameObject.transform.childCount);  
  
        //Load new scene
        EditorSceneManager.NewScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.NewScene.html)(NewSceneSetup.EmptyScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.NewSceneSetup.EmptyScene.html), NewSceneMode.Single[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.NewSceneMode.Single.html));  
  
        //Child is deleted as it was a child of the root GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) that got deleted in the scene transition
        if (child == null)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Child deleted correctly");
        else
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Child was not deleted successfully");
    }
}

```

* * *
