* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.HasFrameBounds.html

#  [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).HasFrameBounds()
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
Validates whether custom bounds can be calculated for this Editor.
Use this to validate if [Editor.OnGetFrameBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.OnGetFrameBounds.html) should be called for this window. The Scene view calls `HasFrameBounds` and `OnGetFrameBounds` when the Frame action is invoked. The Frame action can be called from anywhere, but it is commonly called when you press the F key to frame the selected GameObject. 
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// This example traverses all bones in the hierarchy and calculates bounds for the entire object
public class GameObjectEditorWindow: Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    private bool HasFrameBounds()
    {
        // the result of this function depends on implementation
        // it will most likely be used to evaluate whether bounds
        // can exist for the targets of this Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Window
        return Selection.objects.Length > 0;
    }  
  
    public Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) OnGetFrameBounds()
    {
        Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) bone = Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html);
        Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html) bounds = new Bounds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Bounds.html)(bone.position, new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 0, 0));
        foreach (Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) child in bone)
            bounds.Encapsulate(child.position);  
  
        if (bone.parent) bounds.Encapsulate(bone.parent.position);  
  
        return bounds;
    }
}
```

* * *
