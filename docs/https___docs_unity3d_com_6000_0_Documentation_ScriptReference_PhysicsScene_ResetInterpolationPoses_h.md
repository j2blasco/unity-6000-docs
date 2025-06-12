* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.ResetInterpolationPoses.html

#  [PhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html).ResetInterpolationPoses
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
## Declaration
public void ResetInterpolationPoses(); 
### Description
Resets the [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) positions of interpolated and extrapolated Rigidbodies in this [PhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html) to [Rigidbody.position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-position.html) and [Transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) rotations to [Rigidbody.rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody-rotation.html).
Call this method before simulating to prevent Transform poses of interpolated and extrapolated Rigidbodies from getting synced to the physics system. If multiple [PhysicsScene.Simulate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.Simulate.html) calls are to be made this frame, it's enough to call this method only once, before the first simulation.  
  
This method is called automatically for the default [PhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html) and therefore any manual calls on the [defaultPhysicsScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-defaultPhysicsScene.html) will fail.  
  
Additional resources: [PhysicsScene.InterpolateBodies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.InterpolateBodies.html).
* * *
