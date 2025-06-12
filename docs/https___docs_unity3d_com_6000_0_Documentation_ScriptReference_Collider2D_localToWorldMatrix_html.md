* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-localToWorldMatrix.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).localToWorldMatrix
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
[Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) localToWorldMatrix; 
### Description
The transformation matrix used to transform the Collider physics shapes to world space.
The [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) creates [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) in the space of any attached [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html). The transformation matrix returned here transforms these shapes from the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html)'s local space to world space.  
  
If the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is not attached to a [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) then [Matrix4x4.identity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-identity.html) is returned because the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is Static and the subsequently created [PhysicsShape2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsShape2D.html) will already be in world space.  
  
Additional resources: [Rigidbody2D.localToWorldMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-localToWorldMatrix.html) and [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html).
* * *
