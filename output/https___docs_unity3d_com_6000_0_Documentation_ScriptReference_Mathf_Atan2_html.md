* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Atan2.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).Atan2
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mathf.html "Go to Mathf Component in the Manual")
## Declaration
public static float Atan2(float y, float x); 
### Description
Returns the angle in radians whose [Tan](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Tan.html) is `y/x`.
Return value is the angle between the x-axis and a 2D vector starting at zero and terminating at (x,y).  
  
**Note:** This function takes account of the cases where x is zero and returns the correct angle rather than throwing a division by zero exception.
```
// Usually you use transform.LookAt for this.
// But this can give you more control over the angle  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) target;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) relative = transform.InverseTransformPoint(target.position);
        float angle = Mathf.Atan2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Atan2.html)(relative.x, relative.z) * Mathf.Rad2Deg[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Rad2Deg.html);
        transform.Rotate(0, angle, 0);
    }
}

```

* * *
