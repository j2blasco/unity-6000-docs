* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.GetFiltered.html

#  [Selection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html).GetFiltered
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
public static Object[] GetFiltered(Type type, [SelectionMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.html) mode); 
### Parameters
Parameter | Description  
---|---  
type | Only objects of this type will be retrieved.  
mode | Further options to refine the selection.  
### Description
Returns the current selection filtered by type and mode.
For a selected GameObject that has multiple Components of `type`, only the first one will be included in the results.   
If `type` is a subclass of [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) or [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) the full SelectionMode is supported.   
If `type` does not subclass from [Component](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.html) or [GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) (eg. [Mesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mesh.html) or [ScriptableObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)) only [SelectionMode.ExcludePrefab](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.ExcludePrefab.html) and [SelectionMode.Editable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.Editable.html) are supported.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class ToggleActive : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Toggle.html) Active of Selected %i")]
    static void DoToggle()
    {
        Object[] activeGOs =
            Selection.GetFiltered[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.GetFiltered.html)(
                typeof(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)),
                SelectionMode.Editable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.Editable.html) | SelectionMode.TopLevel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionMode.TopLevel.html));  
  
        foreach (GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) obj in activeGOs)
        {
            obj.SetActive(!obj.activeSelf);
        }
    }
}

```

* * *
