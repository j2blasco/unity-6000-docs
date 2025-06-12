* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawSphere.html

#  [Gizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html).DrawSphere
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
public static void DrawSphere([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center, float radius); 
### Description
Draws a solid sphere with `center` and `radius`.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void OnDrawGizmosSelected()
    {
        // Draw a yellow sphere at the transform's position
        Gizmos.color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos-color.html) = Color.yellow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-yellow.html);
        Gizmos.DrawSphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawSphere.html)(transform.position, 1);
    }
}

```

* * *
