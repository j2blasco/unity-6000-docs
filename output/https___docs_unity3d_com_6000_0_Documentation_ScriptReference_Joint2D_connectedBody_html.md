* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-connectedBody.html

#  [Joint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.html).connectedBody
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
[Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) connectedBody; 
### Description
The Rigidbody2D object to which the other end of the joint is attached (ie, the object without the joint component).
If this property is set to null then the joint attaches to a fixed point in space rather than another Rigidbody2D.  
  
Unity does not support connecting a joint to a [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) in a different [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) that is using a local physics Scene. If a joint is connected to a [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html), and then that [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) is moved to a [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) that uses [LocalPhysicsMode.Physics2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LocalPhysicsMode.Physics2D.html), then the joint is automatically disconnected from the [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html).  
  
Additional resources: [Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html), [LocalPhysicsMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.LocalPhysicsMode.html), [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) and [collideConnected](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D-collideConnected.html).
* * *
