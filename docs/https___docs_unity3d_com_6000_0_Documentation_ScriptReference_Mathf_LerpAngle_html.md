* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.LerpAngle.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).LerpAngle
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
public static float LerpAngle(float a, float b, float t); 
### Parameters
Parameter | Description  
---|---  
a | The start angle. A float expressed in degrees.  
b | The end angle. A float expressed in degrees.  
t | The interpolation value between the start and end angles. This value is clamped to the range [0, 1].  
### Returns
**float** Returns the interpolated float result between angle `a` and angle `b`, based on the interpolation value `t`. 
### Description
Same as [Lerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Lerp.html) but makes sure the values interpolate correctly when they wrap around 360 degrees.
This method returns the shortest path between the specified angles. This method wraps around values that are outside the range [-180, 180]. For example, LerpAngle(1.0f, 190.0f, 1.0f) returns -170.0f. To find the longest path use [Lerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Lerp.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    float minAngle = 0.0f;
    float maxAngle = 90.0f;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        float angle = Mathf.LerpAngle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.LerpAngle.html)(minAngle, maxAngle, Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html));
        transform.eulerAngles = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(0, angle, 0);
    }
}

```

Additional resources: [Lerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Lerp.html).
* * *
