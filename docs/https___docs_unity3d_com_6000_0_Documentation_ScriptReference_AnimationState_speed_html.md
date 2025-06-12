* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState-speed.html

#  [AnimationState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.html).speed
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
speed; 
### Description
The playback speed of the animation. 1 is normal playback speed.
A negative playback speed will play the animation backwards.  
  
Additional resources: [AnimationState.time](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState-time.html), [AnimationState.wrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState-wrapMode.html) properties and [WrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WrapMode.html) enum.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) anim;  
  
    void Start()
    {
        // Walk at normal speed
        anim["Walk"].speed = 1.0f;  
  
        // Walk at double speed
        anim["Walk"].speed = 2.0f;
    }
}

```

* * *
