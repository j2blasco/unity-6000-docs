* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointBreakAction2D.html

# JointBreakAction2D
enumeration
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
Options for selecting which action to take when a [Joint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.html) breaks.
Additional resources: [Joint2D.breakAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-breakAction.html), [Joint2D.breakForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-breakForce.html) or [Joint2D.breakTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-breakTorque.html).
### Properties
Property | Description  
---|---  
[Ignore](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointBreakAction2D.Ignore.html) | When the Joint2D breaks, no action will be taken and Joint2D.OnJointBreak2D will not be called.  
[CallbackOnly](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointBreakAction2D.CallbackOnly.html) | When the Joint2D breaks, call Joint2D.OnJointBreak2D but take no other action.  
[Disable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointBreakAction2D.Disable.html) | When the Joint2D breaks, call Joint2D.OnJointBreak2D and then disable the component.  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointBreakAction2D.Destroy.html) | When the Joint2D breaks, call Joint2D.OnJointBreak2D and then destroy the component.  
* * *
