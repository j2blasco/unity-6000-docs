* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.InverseLerp.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).InverseLerp
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
public static float InverseLerp(float a, float b, float value); 
### Parameters
Parameter | Description  
---|---  
a | The start of the range.  
b | The end of the range.  
value | The point within the range you want to calculate.  
### Returns
**float** A value between zero and one, representing where the "value" parameter falls within the range defined by a and b. 
### Description
Determines where a `value` lies between two points.
The a and b values define the start and end of a linear numeric range. The "value" parameter you supply represents a value which might lie somewhere within that range. This method calculates where, within the specified range, the "value" parameter falls.  
If the "value" parameter is within the range, InverseLerp returns a value between zero and one, proportional to the value's position within the range. If the "value" parameter falls outside of the range, InverseLerp returns either zero or one, depending on whether it falls before the start of the range or after the end of the range.
```
using UnityEngine;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public float start = 20.0f;
    public float end = 40.0f;
    public float currentProgress = 22.0f;  
  
    void Start()
    {
        // the progress between start and end is stored as a 0-1 value, in 'i'
        float i = Mathf.InverseLerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.InverseLerp.html)(start, end, currentProgress);  
  
        // this will display "Current progress: 0.1 or 10%" in Console window
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Current progress: " + i + " or " + i * 100 + "%");  
  
        // the needle of an on-screen dial could then be set to a
        // rotational angle out of 360 degrees, based on the progress.
        float dialNeedleAngle = i * 360;  
  
        //// this will display "Needle angle: 36" in Console window
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Needle angle: " + dialNeedleAngle);
    }
}

```

Additional resources: [Lerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Lerp.html).
* * *
