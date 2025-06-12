* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RecordPrefabInstancePropertyModifications.html

#  [PrefabUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.html).RecordPrefabInstancePropertyModifications
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
public static void RecordPrefabInstancePropertyModifications([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) targetObject); 
### Parameters
Parameter | Description  
---|---  
targetObject | Object to process.  
### Description
Causes modifications made to the Prefab instance to be recorded.
Note that the recommended method of enabling instances of Prefabs to record changes is to use SerializedProperty and SerializedObject. This enables instances to record changes and automatically includes changes in the undo system.  
  
Call this method after making modifications to an instance of a Prefab to record those changes in the instance. If this method is not called, changes made to the instance are lost. Note that if you are not using SerializedProperty/SerializedObject, changes to the object are not recorded in the undo system whether or not this method is called.  
  
Additional resources: [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.SceneManagement;  
  
// The following Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) script doubles the scale of the selected GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html),
// records the property modification and marks the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) as dirty so that
// the user can save the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) afterwards and keep the changes.
public class Example
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Double Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html)")]
    static void DoubleScale()
    {
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject = Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html);
        Undo.RecordObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObject.html)(gameObject.transform, "Double scale");
        gameObject.transform.localScale *= 2;  
  
        // Notice that if the call to RecordPrefabInstancePropertyModifications is not present,
        // all changes to scale will be lost when saving the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html), and reopening the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html)
        // would revert the scale back to its previous value.
        PrefabUtility.RecordPrefabInstancePropertyModifications[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RecordPrefabInstancePropertyModifications.html)(gameObject.transform);  
  
        // Optional step in order to save the Scene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) changes permanently.
        //EditorSceneManager.SaveScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.SaveScene.html)(SceneManager.GetActiveScene[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.GetActiveScene.html)());
    }  
  
    // Disable the menu item if there is no Hierarchy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Hierarchy.Hierarchy.html) GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) selection.
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Double Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html)", true)]
    static bool ValidateDoubleScale()
    {
        return Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html) != null && !EditorUtility.IsPersistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.IsPersistent.html)(Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html));
    }
}

```

* * *
