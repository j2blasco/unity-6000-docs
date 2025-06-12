* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint-breakTorque.html

#  [Joint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint.html).breakTorque
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
breakTorque; 
### Description
The torque that needs to be applied for this joint to break. To be able to break, a joint must be _Locked_ or _Limited_ on the axis of rotation where the torque is being applied. This means that some joints cannot break, such as an unconstrained Configurable Joint.
The torque might come from collisions with other objects, forces applied with [Rigidbody.AddTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.AddTorque.html) or from other joints. The break torque can be set to [Mathf.Infinity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Infinity.html) to render the joint unbreakable. Additional resources: [Joint.OnJointBreak](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint.OnJointBreak.html).
* * *
