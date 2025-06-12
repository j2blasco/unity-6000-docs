* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html

#  [Gizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html).color
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
[Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color; 
### Description
Sets the [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) of the gizmos that are drawn next.
You can apply any color to gizmos. You can make a gizmo transparent by setting the alpha component of [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) to a value lower than 1. The following example shows how to create a red gizmo.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnDrawGizmosSelected()
    {
        // Draws a 5 unit long red line in front of the object
        Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) direction = transform.TransformDirection(Vector3.forward[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-forward.html)) * 5;
        Gizmos.DrawRay[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawRay.html)(transform.position, direction);
    }
}

```

* * *
