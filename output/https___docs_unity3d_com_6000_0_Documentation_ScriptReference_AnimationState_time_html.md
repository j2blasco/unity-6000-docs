* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState-time.html

#  [AnimationState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.html).time
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
The current time of the animation.
If the time is larger than length it will be wrapped according to wrapMode. The value can be larger than the animations length. In this case playback mode will remap the time before sampling. This value usually goes from 0 to infinity.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) anim;  
  
    void Start()
    {
        // Rewind the walk animation
        anim["Walk"].time = 0.0f;
    }
}

```

* * *
