* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetIKPosition.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).GetIKPosition
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
public [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) GetIKPosition([AvatarIKGoal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.html) goal); 
### Parameters
Parameter | Description  
---|---  
goal | The AvatarIKGoal that is queried.  
### Returns
**Vector3** Return the current position of this IK goal in world space. 
### Description
Gets the position of an IK goal.
An IK goal is a target position and rotation for a specific body part. Unity can calculate how to move the part toward the target from the starting point (ie, the current position and rotation obtained from the animation).  
  
This function gets the current position of the specified goal in world space.  
  
Additional resources: [GetIKPositionWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetIKPositionWeight.html), [SetIKPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKPosition.html).
* * *
