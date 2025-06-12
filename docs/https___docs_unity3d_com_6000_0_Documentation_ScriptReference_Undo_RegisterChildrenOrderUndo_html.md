* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RegisterChildrenOrderUndo.html

#  [Undo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.html).RegisterChildrenOrderUndo
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
public static void RegisterChildrenOrderUndo([Object](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.html) objectToUndo, string name); 
### Parameters
Parameter | Description  
---|---  
objectToUndo | The object whose child order should be recorded on the undo stack.  
name | The name of the undo operation.  
### Description
Stores a copy of the order of the object's children on the undo stack.
If the undo is performed, the order of the object's children will be restored to the recorded state.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class UndoExamples
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Undo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.html) Examples/RegisterChildrenOrderUndo")]
    static void Example()
    {
        var parent = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Parent");
        for (int childIndex = 0; childIndex < 5; childIndex += 1)
        {
            var child = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)($"Child{childIndex}");
            child.transform.parent = parent.transform;
        }  
  
        // Store the states of the parent object.
        Undo.RegisterChildrenOrderUndo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RegisterChildrenOrderUndo.html)(parent.transform, "Set as last sibling");
        parent.transform.GetChild(0).SetAsLastSibling();  
  
        // If you choose "Edit->Undo[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.html) Set as last sibling" from the main menu now, the order of the children will be restored.
    }
}

```

* * *
