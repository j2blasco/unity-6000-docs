* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-finishedDefaultHeaderGUI.html

#  [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).finishedDefaultHeaderGUI
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
An event raised while drawing the header of the Inspector window, after the default header items have been drawn.
Add an event handler to this event in order to draw additional items in the header for the [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) passed to the event handler method.  
  
The following example script displays an asset's GUID as a copyable label in the header, if the inspected object is a persistent asset and not a Scene object. Copy this example script into a file called EditorHeaderGUID.cs and put it in a folder called Editor.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/FinishedDefaultHeaderGUI.png) _The Inspector header with a custom GUID control added._
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
[InitializeOnLoadAttribute[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InitializeOnLoadAttribute.html)]
static class EditorHeaderGUID
{
    static EditorHeaderGUID()
    {
        Editor.finishedDefaultHeaderGUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor-finishedDefaultHeaderGUI.html) += DisplayGUIDIfPersistent;
    }  
  
    static void DisplayGUIDIfPersistent(Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) editor)
    {
        if (!EditorUtility.IsPersistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.IsPersistent.html)(editor.target))
            return;  
  
        var guid = AssetDatabase.AssetPathToGUID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AssetPathToGUID.html)(AssetDatabase.GetAssetPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html)(editor.target));
        var totalRect = EditorGUILayout.GetControlRect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.GetControlRect.html)();
        var controlRect = EditorGUI.PrefixLabel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PrefixLabel.html)(totalRect, EditorGUIUtility.TrTempContent("GUID"));
        if (editor.targets.Length > 1)
            EditorGUI.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LabelField.html)(controlRect, EditorGUIUtility.TrTempContent("[Multiple objects selected]"));
        else
            EditorGUI.SelectableLabel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.SelectableLabel.html)(controlRect, guid);
    }
}
```

* * *
