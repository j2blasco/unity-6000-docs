* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Slerp.html

#  [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).Slerp
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
public static [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) Slerp([Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) a, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) b, float t); 
### Parameters
Parameter | Description  
---|---  
a | Start unit quaternion value, returned when t = 0.  
b | End unit quaternion value, returned when t = 1.  
t | Interpolation ratio. Value is clamped to the range [0, 1].  
### Returns
**Quaternion** A unit quaternion spherically interpolated between quaternions `a` and `b`. 
### Description
Spherically linear interpolates between unit quaternions `a` and `b` by a ratio of `t`.
Use this to create a rotation which smoothly interpolates between the first unit quaternion `a` to the second unit quaternion `b`, based on the value of the parameter `t`. If the value of the parameter is close to 0, the output will be close to `a`, if it is close to 1, the output will be close to `b`.
```
// Interpolates rotation between the rotations "from" and "to"
// (Choose from and to not to be the same as
// the object you attach this script to)  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) from;
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) to;  
  
    private float timeCount = 0.0f;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        transform.rotation = Quaternion.Slerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Slerp.html)(from.rotation, to.rotation, timeCount);
        timeCount = timeCount + Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);
    }
}

```

Additional resources: [Lerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Lerp.html), [SlerpUnclamped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.SlerpUnclamped.html).
* * *
