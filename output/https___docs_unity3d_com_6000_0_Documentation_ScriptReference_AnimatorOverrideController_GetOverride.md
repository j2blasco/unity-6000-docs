* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController.GetOverrides.html

#  [AnimatorOverrideController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController.html).GetOverrides
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
## Declaration
public void GetOverrides(List<KeyValuePair<AnimationClip,AnimationClip>> overrides); 
### Parameters
Parameter | Description  
---|---  
overrides | Array to receive results.  
### Description
Gets the list of Animation Clip overrides currently defined in this Animator Override Controller.
This function is allocation-free if you pre-allocate the overrides list with [AnimatorOverrideController.overridesCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController-overridesCount.html).
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;  
  
public class ResetOverrides : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public AnimatorOverrideController[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController.html) overrideController;
    protected List<KeyValuePair<AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html), AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html)>> overrides;  
  
    public void ResetAllOverrides()
    {
        overrides = new List<KeyValuePair<AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html), AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html)>>(overrideController.overridesCount);
        overrideController.GetOverrides(overrides);
        for (int i = 0; i < overrides.Count; ++i)
            overrides[i] = new KeyValuePair<AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html), AnimationClip[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html)>(overrides[i].Key, null);
        overrideController.ApplyOverrides(overrides);
    }
}

```

* * *
