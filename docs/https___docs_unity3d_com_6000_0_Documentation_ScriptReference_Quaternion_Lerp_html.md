* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Lerp.html

#  [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).Lerp
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
public static [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) Lerp([Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) a, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) b, float t); 
### Parameters
Parameter | Description  
---|---  
a | Start unit quaternion value, returned when t = 0.  
b | End unit quaternion value, returned when t = 1.  
t | Interpolation ratio. The value is clamped to the range [0, 1].  
### Returns
**Quaternion** A unit quaternion interpolated between quaternions `a` and `b`. 
### Description
Interpolates between `a` and `b` by `t` and normalizes the result afterwards.
This is faster than Slerp but the angular velocity will not be constant if the rotations are far apart.
```
// Interpolates rotation between the rotations
// of from and to.
// (Choose from and to not to be the same as
// the object you attach this script to)  
  
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) from;
    Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) to;
    float speed = 0.01f;
    float timeCount = 0.0f;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        transform.rotation = Quaternion.Lerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Lerp.html)(from.rotation, to.rotation, timeCount * speed);
        timeCount = timeCount + Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);
    }
}

```

Additional resources: [Slerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Slerp.html). [LerpUnclamped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.LerpUnclamped.html).
* * *
