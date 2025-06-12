* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-transforms.html

#  [Selection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html).transforms
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
transforms; 
### Description
Returns the top level selection, excluding Prefabs.
This is the most common selection type when working with Scene objects.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
class LookAtMainCamera : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Selection[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html) looks at Main Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) _l")]  
  
    static void Look()
    {
        var camera = Camera.main[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-main.html);  
  
        if (camera)
        {
            foreach (Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) transform in Selection.transforms[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-transforms.html))
            {
                Undo.RegisterUndo(transform, transform.name + " Looks at Main Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)");
                transform.LookAt(camera.transform);
            }
        }
    }  
  
    //The menu item will be disabled if nothing is selected.
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/Selection[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection.html) looks at Main Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) _l", true)]
    static bool ValidateSelection()
    {
        return Selection.transforms.Length != 0;
    }
}

```

* * *
