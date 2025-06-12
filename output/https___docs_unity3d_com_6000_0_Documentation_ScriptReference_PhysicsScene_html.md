* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.html

# PhysicsScene
struct in UnityEngine
/
Implemented in:[UnityEngine.PhysicsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.PhysicsModule.html)
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
Represents a single instance of a 3D physics Scene.
### Public Methods
Method | Description  
---|---  
[BoxCast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.BoxCast.html) | Casts the box along a ray and returns detailed information on what was hit.  
[CapsuleCast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.CapsuleCast.html) | Casts a capsule against all colliders in this physics scene and returns detailed information on what was hit.  
[InterpolateBodies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.InterpolateBodies.html) | Interpolates Rigidbodies in this PhysicsScene.  
[IsEmpty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.IsEmpty.html) | Gets whether the physics Scene is empty or not.  
[IsValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.IsValid.html) | Gets whether the physics Scene is valid or not.  
[OverlapBox](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.OverlapBox.html) | Find all colliders touching or inside of the given box, and store them into the buffer.  
[OverlapCapsule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.OverlapCapsule.html) | Check the given capsule against the physics world and return all overlapping colliders in the user-provided buffer.  
[OverlapSphere](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.OverlapSphere.html) | Computes and stores colliders touching or inside the sphere into the provided buffer.  
[Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.Raycast.html) | Casts a ray, from point origin, in direction direction, of length maxDistance, against all colliders in the Scene.  
[ResetInterpolationPoses](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.ResetInterpolationPoses.html) | Resets the Transform positions of interpolated and extrapolated Rigidbodies in this PhysicsScene to Rigidbody.position and Transform rotations to Rigidbody.rotation.  
[RunSimulationStages](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.RunSimulationStages.html) | Runs specified physics simulation stages on this physics scene.  
[Simulate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.Simulate.html) | Simulate physics associated with this PhysicsScene.  
[SphereCast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene.SphereCast.html) | Casts a sphere along a ray and returns detailed information on what was hit.  
* * *
