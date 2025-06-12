* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.RotateTowards.html

#  [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).RotateTowards
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Quaternion.html "Go to Quaternion Component in the Manual")
## Declaration
public static [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) RotateTowards([Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) from, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) to, float maxDegreesDelta); 
### Parameters
Parameter | Description  
---|---  
from | The unit quaternion to be aligned with `to`.  
to | The target unit quaternion.  
maxDegreesDelta | The maximum angle in degrees allowed for this rotation.  
### Returns
**Quaternion** A unit quaternion rotated towards `to` by an angular step of `maxDegreesDelta`. 
### Description
Rotates a rotation `from` towards `to`.
The `from` quaternion is rotated towards `to` by an angular step of `maxDegreesDelta`. The rotation will not overshoot the `to` quaternion. Negative values of `maxDegreesDelta` moves away from `to` until the rotation is exactly the opposite direction.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // The object whose rotation we want to match.
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) target;  
  
    // Angular speed in degrees per sec.
    public float speed = 1.0f;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // The step size is equal to speed times frame time.
        var step = speed * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);  
  
        // Rotate[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Rotate.html) our transform a step closer to the target's.
        transform.rotation = Quaternion.RotateTowards[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.RotateTowards.html)(transform.rotation, target.rotation, step);
    }
}

```

* * *
