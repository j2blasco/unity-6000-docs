* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Animations.AnimationStreamSource.PreviousInputs.html

**Experimental** : this API is experimental and might be changed or removed in the future.
#  [AnimationStreamSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Animations.AnimationStreamSource.html).PreviousInputs
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
### Description
[AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) will be initialized with the values from the previous [AnimationPlayableOutput](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationPlayableOutput.html) connected to the same [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).
Before it is modified during [IAnimationJob.ProcessAnimation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJob.ProcessAnimation.html) or [IAnimationJob.ProcessRootMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.IAnimationJob.ProcessRootMotion.html), the [AnimationStream](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimationStream.html) contains the values written by any previous inputs.  
  
Additional resources: [AnimationPlayableOutputExtensions.SetAnimationStreamSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Animations.AnimationPlayableOutputExtensions.SetAnimationStreamSource.html).
* * *
