* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-applyRootMotion.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).applyRootMotion
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
applyRootMotion; 
### Description
Should root motion be applied?
Root motion is the effect where an object's entire mesh moves away from its starting point but that motion is created by the animation itself rather than by changing the Transform position. Note that `applyRootMotion` has no effect when the script implements a [MonoBehaviour.OnAnimatorMove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnAnimatorMove.html) function.  
  
Changing the value of applyRootMotion at runtime will re-initialize the animator.
* * *
