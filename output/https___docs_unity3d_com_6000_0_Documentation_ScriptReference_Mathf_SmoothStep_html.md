* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.SmoothStep.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).SmoothStep
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
public static float SmoothStep(float from, float to, float t); 
### Parameters
Parameter | Description  
---|---  
from | The start of the range.  
to | The end of the range.  
t | The interpolation value between the `from` and `to` range limits.  
### Returns
**float** The interpolated float result between `from` and `to`. 
### Description
Interpolates between `from` and `to` with smoothing at the limits.
This function interpolates between `from` and `to` in a similar way to [Lerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Lerp.html). However, the interpolation will gradually speed up from the start and slow down toward the end. This is useful for creating natural-looking animation, fading and other transitions.  
  
The parameter `t` is clamped to the range [0, 1].
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Minimum and maximum values for the transition.
    float minimum = 10.0f;
    float maximum = 20.0f;  
  
    // Time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time.html) taken for the transition.
    float duration = 5.0f;  
  
    float startTime;  
  
    void Start()
    {
        // Make a note of the time the script started.
        startTime = Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html);
    }  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        // Calculate the fraction of the total duration that has passed.
        float t = (Time.time[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-time.html) - startTime) / duration;
        transform.position = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(Mathf.SmoothStep[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.SmoothStep.html)(minimum, maximum, t), 0, 0);
    }
}

```

* * *
