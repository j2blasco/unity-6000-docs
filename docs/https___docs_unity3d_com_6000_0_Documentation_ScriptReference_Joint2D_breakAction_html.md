* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-breakAction.html

#  [Joint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.html).breakAction
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
[JointBreakAction2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointBreakAction2D.html) breakAction; 
### Description
The action to take when the joint breaks the [breakForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-breakForce.html) or [breakTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-breakTorque.html).
A joint breaks when the force a joint exerts exceeds [breakForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-breakForce.html) or when the torque a joint exerts exceeds [breakTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-breakTorque.html). The joint action happens after the call to [Joint2D.OnJointBreak2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.OnJointBreak2D.html) has completed. If the [breakAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-breakAction.html) is changed during the [Joint2D.OnJointBreak2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.OnJointBreak2D.html) callback then that updated action happens.  
  
Additional resources: [JointBreakAction2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointBreakAction2D.html).
* * *
