* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.SmoothDamp.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).SmoothDamp
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
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) SmoothDamp([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) current, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) target, ref [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) currentVelocity, float smoothTime, float maxSpeed = Mathf.Infinity, float deltaTime = Time.deltaTime); 
### Parameters
Parameter | Description  
---|---  
current | The current position.  
target | The position we are trying to reach.  
currentVelocity | The current velocity, this value is modified by the function every time you call it.  
smoothTime | Approximately the time it will take to reach the target. A smaller value will reach the target faster.  
maxSpeed | Optionally allows you to clamp the maximum speed.  
deltaTime | The time since the last call to this function. By default Time.deltaTime.  
### Description
Gradually changes a vector towards a desired goal over time.
The vector is smoothed by some spring-damper like function, which will never overshoot. The most common use is for smoothing a follow camera.
```
// Smooth towards the target  
  
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) target;
    public float smoothTime = 0.3F;
    private Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) velocity = Vector3.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-zero.html);  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Define a target position above and behind the target transform
        Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) targetPosition = target.TransformPoint(new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, 5, -10));  
  
        // Smoothly move the camera towards that target position
        transform.position = Vector3.SmoothDamp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.SmoothDamp.html)(transform.position, targetPosition, ref velocity, smoothTime);
    }
}

```

* * *
