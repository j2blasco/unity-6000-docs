* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.CollapseUndoOperations.html

#  [Undo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.html).CollapseUndoOperations
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
public static void CollapseUndoOperations(int groupIndex); 
### Parameters
Parameter | Description  
---|---  
groupIndex | The group index to collapse undo operations to.  
### Description
Collapses all undo operations down to group index together into one step.
The current group index automatically increases on mouse down, by clicking on menu items, and other operations. This method collapses all undo operations with group indices above the provided group index to that group index. This is used by the color picker to combine all color modifications into a single step once the color picker is closed, while they are seperate operations when the color picker is still open.
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;

public class ResetPositionForSelectedGameObjectsExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("MyMenu/Reset Positions of Selected GameObjects")]
    static void ResetPositionForSelectedGameObjects()
    {
        Undo.SetCurrentGroupName[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.SetCurrentGroupName.html)("Zero out selected gameObjects");
        int group = Undo.GetCurrentGroup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.GetCurrentGroup.html)();

        Undo.RecordObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.RecordObjects.html)(Selection.transforms[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-transforms.html), "transform selected objects");

        foreach (Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) t in Selection.transforms[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-transforms.html))
        {
            t.position = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);
        }

        Undo.CollapseUndoOperations[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Undo.CollapseUndoOperations.html)(group);
    }
}

```

* * *
