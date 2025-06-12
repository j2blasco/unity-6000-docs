* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-keepAnimatorStateOnDisable.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).keepAnimatorStateOnDisable
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
keepAnimatorStateOnDisable; 
### Description
Controls the behaviour of the Animator component when a GameObject is inactive.
Set to true to keep the current state of the Animator controller.  
Set to false to clear the current state of the Animator controller.  
The default value is false.  
  
  
**Note** : When this property is set to true, the Animator also preserves the animated values for inactive GameObjects. For example, a GameObject's transform is animated from x=0 to x=3 while it is active. After this GameObject becomes inactive, it still keeps the animated value x=3 instead of x=0.  
  
  
This property is serializable and can be saved in a Prefab.  
This property applies to the AnimatorController associated with the Animator. This property does not affect [AnimatorControllerPlayable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.AnimatorControllerPlayable.html).
* * *
