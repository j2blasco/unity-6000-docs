* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.RemoveMixingTransform.html

#  [AnimationState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.html).RemoveMixingTransform
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
public void RemoveMixingTransform([Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) mix); 
### Description
Removes a transform which should be animated.
You can only pass transforms that have been added through [AddMixingTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.AddMixingTransform.html) function. If transform has been added as `recursive`, then it will be removed as `recursive`. Once you remove all mixing transforms added to animation state all curves become animated again. Additional resources: [AddMixingTransform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimationState.AddMixingTransform.html) function.
* * *
