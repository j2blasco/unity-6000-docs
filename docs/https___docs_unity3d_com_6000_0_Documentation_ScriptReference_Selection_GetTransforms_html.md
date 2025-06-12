* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.GetTransforms.html

#  [Selection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html).GetTransforms
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
public static Transform[] GetTransforms([SelectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.html) mode); 
### Parameters
Parameter | Description  
---|---  
mode | Options for refining the selection.  
### Description
Allows for fine grained control of the selection type using the [SelectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.html) bitmask.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  

class CreateParentForTransforms : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Create Parent For Selection[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html) _p")]
    static void MenuInsertParent()
    {
        Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)[] selection = Selection.GetTransforms[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.GetTransforms.html)(
            SelectionMode.TopLevel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.TopLevel.html) | SelectionMode.Editable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.Editable.html));
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) newParent = new GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)("Parent");  
  
        foreach (Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) t in selection)
        {
            t.parent = newParent.transform;
        }
    }  
  
    // Disable the menu if there is nothing selected
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Create Parent For Selection[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html) _p", true)]
    static bool ValidateSelection()
    {
        return Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html) != null;
    }
}

```

* * *
