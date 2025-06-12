* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SetDirty.html

#  [EditorUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.html).SetDirty
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
public static void SetDirty([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) target); 
### Parameters
Parameter | Description  
---|---  
target | The object to mark as dirty.  
### Description
Marks `target` object as dirty.
You can use [SetDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SetDirty.html) when you want to modify an object without creating an undo entry, but still ensure the change is registered and not lost. If the object is part of a Scene, the Scene is marked dirty. If the object may be part of a Prefab instance, you additionally need to call [PrefabUtility.RecordPrefabInstancePropertyModifications](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RecordPrefabInstancePropertyModifications.html) to ensure a Prefab override is created.  
  
If you do want to support undo, you should not call [SetDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SetDirty.html) but rather use [Undo.RecordObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObject.html) prior to making changes to an object, since this will both mark the object as dirty (or the object's Scene if it is part of a Scene) and provide an undo entry in the editor. You should still also call [PrefabUtility.RecordPrefabInstancePropertyModifications](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrefabUtility.RecordPrefabInstancePropertyModifications.html) if the object may be part of a Prefab instance.  
  
In the case of [ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html), call both [SetDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SetDirty.html) and [Undo.RecordObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObject.html), if you want to register the change and support undo.  
  
When you create editor UI for manipulating an object, such as a custom editor to modify serialized properties on a component or asset, if possible, you should use the [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) system using [SerializedObject.FindProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.FindProperty.html), [SerializedObject.Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.Update.html), [EditorGUILayout.PropertyField](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PropertyField.html), and [SerializedObject.ApplyModifiedProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.ApplyModifiedProperties.html). This will automatically mark the object as dirty, create an undo entry, and ensure Prefab overrides are created if relevant.  
  
Additional resources: [GetDirtyCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.GetDirtyCount.html), [IsDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.IsDirty.html).
* * *
