* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-targetPosition.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).targetPosition
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) targetPosition; 
### Description
Returns the position of the target specified by [SetTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetTarget.html).
The position is only valid when a frame is being evaluated after the [SetTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetTarget.html) call. [Animator.applyRootMotion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-applyRootMotion.html) must be enabled for targetPosition to be calculated.
* * *
