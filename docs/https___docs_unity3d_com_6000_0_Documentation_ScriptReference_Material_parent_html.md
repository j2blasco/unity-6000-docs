* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-parent.html

#  [Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html).parent
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html "Go to Material Component in the Manual")
[Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) parent; 
### Description
Parent of this material.
Materials with a non null parent are referred to as material variants.  
  
Material variants will inherit all their properties from their parent, and can override them on a per property basis. Changing the value of a property of a material will therefore impact all variants below in the hierarchy.  
  
This property is only available in the Editor, in a built project all material hierarchies are flattened.  
  
Additional resources: [Material.IsChildOf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.IsChildOf.html), [Material.IsPropertyOverriden](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.IsPropertyOverriden.html), [Material.IsPropertyLocked](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.IsPropertyLocked.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
#if UNITY_EDITOR
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)/Create Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) Variant[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ToolbarMenu.Variant.html)")]
    static void DuplicateMaterial()
    {
        Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) selected = Selection.activeObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeObject.html) as Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html);
        if (selected == null)
            return;  
  
        // Create a material variant from selected material
        // And override it's color to red
        Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material = new Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html)(selected);
        material.parent = selected;
        material.color = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);  
  
        AssetDatabase.CreateAsset[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html)(material, "Assets/" + selected.name + " Variant.mat");
    }
#endif
}
```

* * *
