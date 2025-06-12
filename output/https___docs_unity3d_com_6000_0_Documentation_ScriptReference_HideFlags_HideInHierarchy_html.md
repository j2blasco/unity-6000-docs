* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideInHierarchy.html

#  [HideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.html).HideInHierarchy
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
The object will not appear in the hierarchy.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Creates 5 planes and hides them from the Hierarchy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.Hierarchy.html) in the Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html).  
  
    void Start()
    {
        for (int i = 0; i < 5; i++)
        {
            GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) createdGO = GameObject.CreatePrimitive[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CreatePrimitive.html)(PrimitiveType.Plane[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PrimitiveType.Plane.html));
            createdGO.hideFlags = HideFlags.HideInHierarchy[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HideFlags.HideInHierarchy.html);
        }
    }
}

```

* * *
