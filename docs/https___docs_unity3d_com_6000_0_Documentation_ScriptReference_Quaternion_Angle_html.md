* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Angle.html

#  [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).Angle
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
public static float Angle([Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) a, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) b); 
### Description
Returns the angle in degrees between two rotations `a` and `b`. The resulting angle ranges from 0 to 180.
Example: Think of two GameObjects (A and B) moving around a third GameObject (C). Lines from C to A and C to B create a triangle which can change over time. The angle between CA and CB is the value [Quaternion.Angle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Angle.html) provides.
```
using UnityEngine;
using System.Collections;  
  
// Calculates the angle (degrees) between
// the rotation of this transform and target.  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) target;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        float angle = Quaternion.Angle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Angle.html)(transform.rotation, target.rotation);
    }
}

```

* * *
