* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.NotEditable.html

#  [HideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.html).NotEditable
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
The object is not editable in the Inspector.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Create a plane and dont let it be modificable in the Inspector
    // nor in the Sceneview.  
  
    void Start()
    {
        GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) createdGO = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Plane.html));
        createdGO.hideFlags = HideFlags.NotEditable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.NotEditable.html);
    }
}

```

* * *
