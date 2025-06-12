* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-saveChangesMessage.html

#  [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).saveChangesMessage
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
saveChangesMessage; 
### Description
The message that displays to the user if they are prompted to save.
Set saveChangesMessage in a derived class to prevent users from accidentally losing unsaved work. For saveChangesMessage to work, you must use it with [Editor.hasUnsavedChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-hasUnsavedChanges.html) and override the [Editor.SaveChanges](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.SaveChanges.html) method. This message shows exactly as you have written it. This message presents to users who have unsaved changes, if they attempt to close the Inspector, change Selection or enter Playmode. The save changes message might combine with other messages from other editors. This occurs if there are multiple editors that have unsaved changes.
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
