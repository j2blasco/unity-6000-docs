* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Lerp.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).Lerp
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
public static float Lerp(float a, float b, float t); 
### Parameters
Parameter | Description  
---|---  
a | The start value.  
b | The end value.  
t | The interpolation value between the two floats.  
### Returns
**float** The interpolated float result between the two float values. 
### Description
Linearly interpolates between `a` and `b` by `t`.
The parameter `t` is clamped to the range [0, 1].  
  
When `t` = 0 returns `a`.   
When `t` = 1 return `b`.   
When `t` = 0.5 returns the midpoint of `a` and `b`.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // animate the game object from -1 to +1 and back
    public float minimum = -1.0F;
    public float maximum =  1.0F;  
  
    // starting value for the Lerp
    static float t = 0.0f;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // animate the position of the game object...
        transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(Mathf.Lerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Lerp.html)(minimum, maximum, t), 0, 0);  
  
        // .. and increase the t interpolater
        t += 0.5f * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html);  
  
        // now check if the interpolator has reached 1.0
        // and swap maximum and minimum so game object moves
        // in the opposite direction.
        if (t > 1.0f)
        {
            float temp = maximum;
            maximum = minimum;
            minimum = temp;
            t = 0.0f;
        }
    }
}

```

Additional resources: [LerpUnclamped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.LerpUnclamped.html), [LerpAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.LerpAngle.html), [InverseLerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.InverseLerp.html).
* * *
