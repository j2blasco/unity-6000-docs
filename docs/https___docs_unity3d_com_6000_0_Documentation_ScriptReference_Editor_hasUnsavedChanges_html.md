* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-hasUnsavedChanges.html

#  [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).hasUnsavedChanges
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
hasUnsavedChanges; 
### Description
This property specifies whether the Editor prompts the user to save or discard unsaved changes before the Inspector gets rebuilt.
Set hasUnsavedChanges to true to prompt the user to save or discard unsaved changes. This helps prevent them from accidentally losing unsaved work. When you use hasUnsavedChanges, you must also use [EditorWindow.saveChangesMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow-saveChangesMessage.html), and override the [EditorWindow.SaveChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.SaveChanges.html) and/or [EditorWindow.DiscardChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.DiscardChanges.html) methods. When hasUnsavedChanges is enabled, the title bar and docked tabs update to indicate that the user needs to save their work. If the user closes the InspectorWindow, change selection or enters playmode without saving, a message box appears, and prompts them to either save, discard their changes, or cancel.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
[CreateAssetMenu]
public class UnsavedChangesExampleSO : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{}  
  
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(UnsavedChangesExampleSO))]
public class UnsavedChangesExampleEditor : UnityEditor.Editor
{
    void OnEnable()
    {
        saveChangesMessage = "This editor has unsaved changes. Would you like to save?";
    }  
  
    void OnInspectorGUI()
    {
        saveChangesMessage = EditorGUILayout.TextField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.TextField.html)(saveChangesMessage);  
  
        EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)(hasUnsavedChanges ? "I have changes!" : "No changes.", EditorStyles.wordWrappedLabel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorStyles-wordWrappedLabel.html));
        EditorGUILayout.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.LabelField.html)("Try to change selection.");  
  
        using (new EditorGUI.DisabledScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DisabledScope.html)(hasUnsavedChanges))
        {
            if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Create unsaved changes"))
                hasUnsavedChanges = true;
        }  
  
        using (new EditorGUI.DisabledScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DisabledScope.html)(!hasUnsavedChanges))
        {
            if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Save"))
                SaveChanges();  
  
            if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Discard"))
                DiscardChanges();
        }
    }  
  
    public override void SaveChanges()
    {
        // Your custom save procedures here  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{this} saved successfully!!!");
        base.SaveChanges();
    }  
  
    public override void DiscardChanges()
    {
        // Your custom procedures to discard changes  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{this} discarded changes!!!");
        base.DiscardChanges();
    }
}

```

* * *
