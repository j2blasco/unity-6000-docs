* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetIKRotation.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).GetIKRotation
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
public [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) GetIKRotation([AvatarIKGoal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.html) goal); 
### Parameters
Parameter | Description  
---|---  
goal | The AvatarIKGoal that is is queried.  
### Description
Gets the rotation of an IK goal.
An IK goal is a target position and rotation for a specific body part. Unity can calculate how to move the part toward the target from the starting point (ie, the current position and rotation obtained from the animation).  
  
This function gets the current rotation of the specified goal in world space.  
  
Additional resources: [GetIKRotationWeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetIKRotationWeight.html), [SetIKRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKRotation.html).
* * *
