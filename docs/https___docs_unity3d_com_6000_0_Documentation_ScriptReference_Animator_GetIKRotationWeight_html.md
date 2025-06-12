* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetIKRotationWeight.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).GetIKRotationWeight
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
public float GetIKRotationWeight([AvatarIKGoal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarIKGoal.html) goal); 
### Parameters
Parameter | Description  
---|---  
goal | The AvatarIKGoal that is queried.  
### Description
Gets the rotational weight of an IK goal (0 = rotation before IK, 1 = rotation at the IK goal).
An IK goal is a target position and rotation for a specific body part. Unity can calculate how to move the part toward the target from the starting point (ie, the current position and rotation obtained from the animation).  
  
The rotation calculated by the IK is also influenced by a weight value in the range 0..1 that determines how far between the start and the goal to aim. This function returns the current weight value for the rotation of the goal.  
  
Additional resources: [GetIKRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.GetIKRotation.html), [SetIKRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetIKRotation.html).
* * *
