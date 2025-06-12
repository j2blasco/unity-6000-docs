* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState-enabled.html

#  [AnimationState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.html).enabled
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
enabled; 
### Description
Enables / disables the animation.
For the animation to take any effect the weight also needs to be set to a value higher than zero. If the animation is disabled, time will be paused until the animation is enabled again.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) anim;  
  
    void Start()
    {
        // Enable the walk cycle
        anim["Walk"].enabled = true;
        anim["Walk"].weight = 1.0f;
    }
}

```

* * *
