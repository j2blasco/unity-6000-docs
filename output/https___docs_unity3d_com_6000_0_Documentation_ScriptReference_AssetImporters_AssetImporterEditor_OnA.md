* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor.OnApplyRevertGUI.html

#  [AssetImporterEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.AssetImporterEditor.html).OnApplyRevertGUI
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
protected bool OnApplyRevertGUI(); 
### Returns
**bool** Returns true if the new settings were successfully applied. 
### Description
Process the 'Apply' and 'Revert' buttons.
This is called by ApplyRevertGUI to place and handle the 'Apply' and 'Revert' buttons.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.AssetImporters;  
  
public class ExampleScript : ScriptedImporterEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetImporters.ScriptedImporterEditor.html)
{
    public override void OnInspectorGUI()
    {
        serializedObject.Update();  
  
        // Draw custom GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html)  
  
        serializedObject.ApplyModifiedProperties();
        ApplyRevertGUI();
    }  
  
    private bool CanApply()
    {
        // Add custom checks that make sure the Importer is in a valid state to be applied.
        return false;
    }  
  
    protected virtual bool OnApplyRevertGUI()
    {
        using (new EditorGUI.DisabledScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DisabledScope.html)(!HasModified()))
        {
            RevertButton();
            using (new EditorGUI.DisabledScope[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.DisabledScope.html)(!CanApply()))
            {
                return ApplyButton();
            }
        }
    }
}

```

* * *
