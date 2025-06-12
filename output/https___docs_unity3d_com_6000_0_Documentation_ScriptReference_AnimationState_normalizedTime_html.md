* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState-normalizedTime.html

#  [AnimationState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.html).normalizedTime
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
normalizedTime; 
### Description
Normalized time of the State.
The normalized time is a progression ratio. The integer part is the number of times the State has looped. The fractional part is a percentage (0-1) that represents the progress of the current loop. For example, a normalized time of 0.5 means that the State has not looped (0) and is halfway (50% or .5) through the first loop.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) anim;  
  
    void Start()
    {
        // Fast forward to the middle of the animation
        anim["Walk"].normalizedTime = 0.5f;
    }
}

```

* * *
