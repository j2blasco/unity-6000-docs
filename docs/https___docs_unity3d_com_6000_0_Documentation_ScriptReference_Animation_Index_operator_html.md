* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.Index_operator.html

#  [Animation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html).this[string]
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animation.html "Go to Animation Component in the Manual")
[AnimationState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.html) this[string]; 
### Description
Returns the animation state named `name`.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) anim;  
  
    void Start()
    {
        // Get the walk animation state  and set its speed
        anim["walk"].speed = 2.0f;  
  
        // Get the run animation state and set its weight
        anim["run"].weight = 0.5f;
    }
}

```

* * *
