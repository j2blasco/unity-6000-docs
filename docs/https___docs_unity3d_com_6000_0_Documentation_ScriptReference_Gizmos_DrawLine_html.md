* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLine.html

#  [Gizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html).DrawLine
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
public static void DrawLine([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) from, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) to); 
### Description
Draws a line starting at `from` towards `to`.
If you need to draw many lines consider the [Gizmos.DrawLineList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLineList.html) or [Gizmos.DrawLineStrip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLineStrip.html) functions which are much faster than repeatedly calling this function to draw lines individually.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) target;  
  
    void OnDrawGizmosSelected()
    {
        if (target != null)
        {
            // Draws a blue line from this transform to the target
            Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html);
            Gizmos.DrawLine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLine.html)(transform.position, target.position);
        }
    }
}

```

Additional resources: [Gizmos.DrawLineList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLineList.html), [Gizmos.DrawLineStrip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawLineStrip.html).
* * *
