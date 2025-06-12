* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController.Index_operator.html

#  [AnimatorOverrideController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController.html).this[string]
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
[AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) this[string]; 
[AnimationClip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationClip.html) this[AnimationClip]; 
### Description
Returns either the overriding Animation Clip if set or the original Animation Clip named name.
Note: You should avoid calling this function more than once per frame per Animator as each call will trigger a reallocation of the animator's clip bindings. Instead use [AnimatorOverrideController.ApplyOverrides](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorOverrideController.ApplyOverrides.html).
* * *
