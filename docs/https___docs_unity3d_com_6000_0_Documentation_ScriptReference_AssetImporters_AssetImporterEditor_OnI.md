* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor.OnInspectorGUI.html

#  [AssetImporterEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor.html).OnInspectorGUI
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
public void OnInspectorGUI(); 
### Description
Override this method to create your own Inpsector GUI for a ScriptedImporter.
For the OnInspectorGUI Undo/Redo and cancel feature to work in the Inspector, you must either call ApplyRevertGUI or override needsApplyRevert to return false.  
  
Example of an InspectorGUI using ApplyRevertGUI:
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.AssetImporters;
using UnityEngine;  
  
public class CustomInspector : ScriptedImporterEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporterEditor.html)
{
    SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) myProperty;  
  
    public override void OnEnable()
    {
        base.OnEnable();  
  
        myProperty = serializedObject.FindProperty("m_MyProperty");
    }  
  
    public override void OnInspectorGUI()
    {
        serializedObject.Update();  
  
        EditorGUILayout.PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PropertyField.html)(myProperty);  
  
        serializedObject.ApplyModifiedProperties();  
  
        ApplyRevertGUI();
    }
}

```

Example of an InspectorGUI where the user cannot change anything and does not require an ApplyRevertGUI:
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.AssetImporters;
using UnityEngine;  
  
public class CustomInspector : ScriptedImporterEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporterEditor.html)
{
    SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) myProperty;  
  
    public override void OnEnable()
    {
        base.OnEnable();  
  
        myProperty = serializedObject.FindProperty("m_MyProperty");
    }  
  
    protected override bool needsApplyRevert => false;  
  
    public override void OnInspectorGUI()
    {
        serializedObject.Update();  
  
        EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)(myProperty.displayName, myProperty.stringValue);  
  
        serializedObject.ApplyModifiedProperties();
    }
}

```

* * *
