* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.CapsuleGeometry.html

# CapsuleGeometry
struct in UnityEngine.LowLevelPhysics
/
Implemented in:[UnityEngine.PhysicsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.PhysicsModule.html)
Leave feedback
  

Implements interfaces:[IGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.IGeometry.html)
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
Contains the basic geometric shape of a capsule.
When Unity retrieves the geometry from the [CapsuleCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CapsuleCollider.html), the [CapsuleCollider.direction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CapsuleCollider-direction.html) is not included. For this reason, you should assume the direction is always along the X axis.
### Properties
Property | Description  
---|---  
[GeometryType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.CapsuleGeometry.GeometryType.html) | Returns the geometry type of this shape, which is CapsuleGeometry.  
[HalfLength](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.CapsuleGeometry.HalfLength.html) | The distance from the center of the shape to the center of either half-sphere at the caps.  
[Radius](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.CapsuleGeometry.Radius.html) | The radius of the half-sphere at either cap of the capsule.  
### Constructors
Constructor | Description  
---|---  
[CapsuleGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LowLevelPhysics.CapsuleGeometry-ctor.html) | Create a capsule shape with the provided parameters.  
* * *
