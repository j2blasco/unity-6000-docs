* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyType2D.Dynamic.html

#  [RigidbodyType2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyType2D.html).Dynamic
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
Sets the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) to have dynamic behaviour.
Dynamic behaviour causes the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) to react to gravity and applied forces including contacts with other dynamic or [Kinematic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyType2D.Kinematic.html) [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).  
  
This type of [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) should be moved using forces and never repositioned explicitly.  
  
A dynamic [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) will collide with all other [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) body types.  
  
When an attached [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is set to trigger, it will always produce a trigger for any [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) attached to all other [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) body types.  
  
Additional resources: [Rigidbody2D.bodyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-bodyType.html).
* * *
