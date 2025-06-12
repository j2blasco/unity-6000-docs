* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip-legacy.html

#  [AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html).legacy
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html "Go to AnimationClip Component in the Manual")
legacy; 
### Description
Set to true if the AnimationClip will be used with the Legacy Animation component ( instead of the Animator ).
```
using UnityEngine;
using System.Collections;  
  
public class animFov : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) fovc = new AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html)();
        AnimationCurve[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.html) curve = AnimationCurve.Linear[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationCurve.Linear.html)(0.0f, 60.0f, 10.0f, 90.0f);
        fovc.SetCurve("", typeof(Camera[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html)), "field of view", curve);
        fovc.legacy = true;
        GetComponent<Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html)>().AddClip(fovc, "animfov");  
  
        GetComponent<Animation[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animation.html)>().Play("animfov");
    }
}

```

* * *
