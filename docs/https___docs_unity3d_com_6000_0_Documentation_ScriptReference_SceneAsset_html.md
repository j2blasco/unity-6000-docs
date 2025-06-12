* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneAsset.html

# SceneAsset
class in UnityEditor
/
Inherits from:[Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html)
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
SceneAsset is used to reference Scene objects in the Editor.
This can be used as the type for ObjectField UI elements, to allow the user to pick a Scene object as the value of the field.  
  
This example shows how to pick a Scene in the editor. The ScenePicker component is placed on a game object in the Scene:
```
using UnityEngine;  
  
public class ScenePicker : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    public string scenePath;
}

```

The ScenePickerEditor script must be in the Editor directory of the project. It provides the custom inspector in the editor that uses the SceneAsset class in an ObjectField to allow the user to pick a Scene.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(ScenePicker), true)]
public class ScenePickerEditor : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    public override void OnInspectorGUI()
    {
        var picker = target as ScenePicker;
        var oldScene = AssetDatabase.LoadAssetAtPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html)<SceneAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneAsset.html)>(picker.scenePath);  
  
        serializedObject.Update();  
  
        EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();
        var newScene = EditorGUILayout.ObjectField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ObjectField.html)("scene", oldScene, typeof(SceneAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneAsset.html)), false) as SceneAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneAsset.html);  
  
        if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
        {
            var newPath = AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(newScene);
            var scenePathProperty = serializedObject.FindProperty("scenePath");
            scenePathProperty.stringValue = newPath;
        }
        serializedObject.ApplyModifiedProperties();
    }
}

```

### Inherited Members
### Properties
Property | Description  
---|---  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
