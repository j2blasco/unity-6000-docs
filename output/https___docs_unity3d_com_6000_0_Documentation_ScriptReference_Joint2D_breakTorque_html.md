* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-breakTorque.html

#  [Joint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.html).breakTorque
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
The torque that needs to be applied for this joint to break.
When a joint tries to constrain a [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) it may need to apply torque to do so. This is known as the [reactionTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-reactionTorque.html). Each physics update, the [breakTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-breakTorque.html) is compared to the [reactionTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-reactionTorque.html); if it exceeds it then [Joint2D.OnJointBreak2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.OnJointBreak2D.html) is called with a reference to the joint that broke. Knowing the joint that broke you can check the actual reaction torque that broke the joint using [reactionTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-reactionTorque.html) or [Joint2D.GetReactionTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.GetReactionTorque.html).  
  
The break torque can be set to [Mathf.Infinity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Infinity.html) to make the joint unbreakable by any amount of reaction torque. Alternately, setting the [breakAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-breakAction.html) to [JointBreakAction2D.Ignore](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointBreakAction2D.Ignore.html) will make the joint unbreakable by either [breakForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-breakForce.html) or [breakTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-breakTorque.html).  
  
The action taken when a joint exceeds the breakForce is controlled by [breakAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-breakAction.html).  
  
Note: [breakTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-breakTorque.html) is not available on [DistanceJoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DistanceJoint2D.html), [SpringJoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SpringJoint2D.html) or [TargetJoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TargetJoint2D.html).  
  
Additional resources: [Joint2D.reactionTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-reactionTorque.html), [Joint2D.GetReactionTorque](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.GetReactionTorque.html) & [Joint2D.OnJointBreak2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.OnJointBreak2D.html).
* * *
