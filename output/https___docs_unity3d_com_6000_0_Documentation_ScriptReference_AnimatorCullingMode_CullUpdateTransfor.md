* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorCullingMode.CullUpdateTransforms.html

#  [AnimatorCullingMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AnimatorCullingMode.html).CullUpdateTransforms
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
Retarget, IK and write of Transforms are disabled when renderers are not visible.
The statemachine and root motion will always be evaluated. Thus you will always receive the OnAnimatorMove callbacks. All other animation will be skipped if the character is not visible. Specifically evaluation of bone animation, IK, OnAnimatorIK will be skipped.  
  
Note that animation will still be visible in the Scene view, ie it is not affected by animation culling.
* * *
