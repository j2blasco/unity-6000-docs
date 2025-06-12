* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.SmoothDamp.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).SmoothDamp
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
public static float SmoothDamp(float current, float target, ref float currentVelocity, float smoothTime, float maxSpeed = Mathf.Infinity, float deltaTime = Time.deltaTime); 
### Parameters
Parameter | Description  
---|---  
current | The current value.  
target | The target value.  
currentVelocity | Use this parameter to specify the initial velocity to move the current value towards the target value. This method updates the currentVelocity based on this movement and smooth-damping.  
smoothTime | The approximate time it takes for the current value to reach the target value. The lower the smoothTime, the faster the current value reaches the target value. The minimum smoothTime is 0.0001. If a lower value is specified, it is clamped to the minimum value.  
maxSpeed | Use this optional parameter to specify a maximum speed. By default, the maximum speed is set to infinity.  
deltaTime | The time since this method was last called. By default, this is set to `Time.deltaTime`.  
### Returns
**float** The current value after moving one step towards the target value. 
### Description
Gradually moves the current value towards a target value, over a specified time and at a specified velocity.
This method smoothes the current value towards a target value with a spring-damper like algorithm. This algorithm is based on Game Programming Gems 4, Chapter 1.10.  
  
**Note:** This method attempts to avoid overshooting the target value. When deltaTime is 0.0f, this yields NaN for the currentVelocity. If you call back with a currentVelocity of NaN, this method returns a NaN.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Smooth towards the height of the target  
  
    public Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) target;
    float smoothTime = 0.3f;
    float yVelocity = 0.0f;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        float newPosition = Mathf.SmoothDamp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.SmoothDamp.html)(transform.position.y, target.position.y, ref yVelocity, smoothTime);
        transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(transform.position.x, newPosition, transform.position.z);
    }
}

```

* * *
