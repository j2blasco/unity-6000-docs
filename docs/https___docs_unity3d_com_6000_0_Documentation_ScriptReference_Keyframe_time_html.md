* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe-time.html

#  [Keyframe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe.html).time
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
time; 
### Description
The time of the keyframe.
In a 2D graph you could think of this as the x-value.  
  
Additional resources: [value](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Keyframe-value.html).
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curve = AnimationCurve.Linear[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.Linear.html)(0, 0, 5, 5);
        // Extract the time from the first keyframe of a curve
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(curve[0].time);
    }
}

```

* * *
