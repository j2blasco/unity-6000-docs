* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState-normalizedSpeed.html

#  [AnimationState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.html).normalizedSpeed
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
normalizedSpeed; 
### Description
The normalized playback speed.
This is most commonly used to synchronize playback speed when blending between two animations. In most cases it is easier and better to use [Animation Layer syncing](https://docs.unity3d.com/6000.0/Documentation/Manual/AnimationLayers.html) instead.
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html) anim;  
  
    void Start()
    {
        anim = GetComponent<Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html)>();
        anim["Run"].normalizedSpeed = anim["Walk"].normalizedSpeed;
    }
}

```

* * *
