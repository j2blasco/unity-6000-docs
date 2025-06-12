* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.MatchTarget.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).MatchTarget
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Animator.html "Go to Animator Component in the Manual")
## Declaration
public void MatchTarget([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) matchPosition, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) matchRotation, [AvatarTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarTarget.html) targetBodyPart, [MatchTargetWeightMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MatchTargetWeightMask.html) weightMask, float startNormalizedTime, float targetNormalizedTime = 1); 
### Parameters
Parameter | Description  
---|---  
matchPosition | The position we want the body part to reach.  
matchRotation | The rotation in which we want the body part to be.  
targetBodyPart | The body part that is involved in the match.  
weightMask | Structure that contains weights for matching position and rotation.  
startNormalizedTime | Start time within the animation clip (0 - beginning of clip, 1 - end of clip).  
targetNormalizedTime | End time within the animation clip (0 - beginning of clip, 1 - end of clip), values greater than 1 can be set to trigger a match after a certain number of loops. Ex: 2.3 means at 30% of 2nd loop.  
completeMatch | Allows you to specify what should happen if the MatchTarget function is interrupted. A value of true causes the GameObject to immediately move to the matchPosition if interrupted. A value of false causes the GameObject to stay at its current position if interrupted.  
### Description
Automatically adjust the `GameObject` position and rotation.
Adjust the `GameObject` position and rotation so that the AvatarTarget reaches the matchPosition when the current state is at the specified progress. Target matching only works on the base layer (index 0). You can only queue one match target at a time and you must wait for the first one to finish, otherwise your target matching will be discarded. If you call a [MatchTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.MatchTarget.html) with a start time lower than the clip's normalized time and the clip can loop, [MatchTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.MatchTarget.html) will adjust the time to match the next clip loop. For example, start time= 0.2 normalized time = 0.3, start time will be 1.2. [Animator.applyRootMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-applyRootMotion.html) must be enabled for MatchTarget to take effect.
```
using UnityEngine;  
  
public class TargetMatchingManager : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public void MatchTarget(Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) matchPosition, Quaternion[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) matchRotation, AvatarTarget[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarTarget.html) target, MatchTargetWeightMask[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MatchTargetWeightMask.html) weightMask, float normalisedStartTime, float normalisedEndTime)
    {
        var animator = GetComponent<Animator[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html)>();  
  
        if (animator.isMatchingTarget)
            return;  
  
        float normalizeTime = Mathf.Repeat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Repeat.html)(animator.GetCurrentAnimatorStateInfo(0).normalizedTime, 1f);  
  
        if (normalizeTime > normalisedEndTime)
            return;  
  
        animator.MatchTarget(matchPosition, matchRotation, target, weightMask, normalisedStartTime, normalisedEndTime);
    }
}

```

* * *
