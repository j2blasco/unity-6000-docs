* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState-wrapMode.html

#  [AnimationState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.html).wrapMode
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
[WrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WrapMode.html) wrapMode; 
### Description
Wrapping mode of the animation.
By default wrapMode is initialized to the value set in the [Animation component's](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animation.html) wrap mode.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) anim;  
  
    void Start()
    {
        // Set the wrap mode of the walk animation to loop
        anim["Walk"].wrapMode = WrapMode.Loop[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WrapMode.Loop.html);
    }
}

```

* * *
