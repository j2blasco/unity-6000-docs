* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.SetTarget.html

#  [Animator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator.html).SetTarget
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
public void SetTarget([AvatarTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AvatarTarget.html) targetIndex, float targetNormalizedTime); 
### Parameters
Parameter | Description  
---|---  
targetIndex | The avatar body part that is queried.  
targetNormalizedTime | The current state Time that is queried.  
### Description
Sets an AvatarTarget and a targetNormalizedTime for the current state.
Once the frame is evaluated, use [Animator.targetPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-targetPosition.html) and [Animator.targetRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animator-targetRotation.html) to query the position and rotation.
* * *
