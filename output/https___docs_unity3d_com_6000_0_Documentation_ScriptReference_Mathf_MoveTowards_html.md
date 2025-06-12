* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.MoveTowards.html

#  [Mathf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.html).MoveTowards
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
public static float MoveTowards(float current, float target, float maxDelta); 
### Parameters
Parameter | Description  
---|---  
current | The current value.  
target | The value to move towards.  
maxDelta | The maximum change applied to the current value.  
### Description
Moves a value `current` towards `target`.
This function is similar [Mathf.Lerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Lerp.html) except that this function ensures the rate of change never exceeds `maxDelta` and that the current value is never greater than the `target` value. Negative values of `maxDelta` pushes the value away from `target`.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    float currStrength;
    float maxStrength;
    float recoveryRate;  
  
    void Update[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerLoop.Update.html)()
    {
        currStrength = Mathf.MoveTowards[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.MoveTowards.html)(currStrength, maxStrength, recoveryRate * Time.deltaTime[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-deltaTime.html));
    }
}

```

* * *
