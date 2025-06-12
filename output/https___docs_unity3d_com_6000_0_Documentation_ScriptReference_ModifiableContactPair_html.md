* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.html

# ModifiableContactPair
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
A light-weight proxy that allows to access the contact buffers directly.
### Properties
Property | Description  
---|---  
[bodyAngularVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair-bodyAngularVelocity.html) | Angular velocity of the first body in the contact pair.  
[bodyInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair-bodyInstanceID.html) | Instance ID of the first body in this contact pair.  
[bodyVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair-bodyVelocity.html) | Linear velocity of the first body in the contact pair.  
[colliderInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair-colliderInstanceID.html) | Instance ID of the first Collider in this contact pair.  
[contactCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair-contactCount.html) | The amount of the contact points generated for this contact pair.  
[massProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair-massProperties.html) | Mass-related properties of this contact pair, such as the mass ratio.  
[otherBodyAngularVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair-otherBodyAngularVelocity.html) | Angular velocity of the second body in the contact pair.  
[otherBodyInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair-otherBodyInstanceID.html) | Instance ID of the second body in this contact pair.  
[otherBodyVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair-otherBodyVelocity.html) | Linear velocity of the second body in the contact pair.  
[otherColliderInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair-otherColliderInstanceID.html) | Instance ID of the second collider in this contact pair.  
[otherPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair-otherPosition.html) | World-space position of the second collider in this contact pair as seen by the solver.  
[otherRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair-otherRotation.html) | World-space rotation of the second collider in this contact pair as seen by the solver.  
[position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair-position.html) | World-space position of the first collider in this contact pair as seen by the solver.  
[rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair-rotation.html) | World-space rotation of the first collider in this contact pair as seen by the solver.  
### Public Methods
Method | Description  
---|---  
[GetBounciness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.GetBounciness.html) | Get the restitution value for the specified contact point in this contact pair.  
[GetDynamicFriction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.GetDynamicFriction.html) | Get the value of the dynamic friction for a specified contact point in this contact pair.  
[GetFaceIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.GetFaceIndex.html) | Get the index of a face a particular contact point belongs to in this contact pair. Use this with Mesh.triangles.  
[GetMaxImpulse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.GetMaxImpulse.html) | Get the maximum impulse that the solver can apply at a particular contact point in this contact pair.  
[GetNormal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.GetNormal.html) | Get the normal at a particular contact point in this contact pair.  
[GetPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.GetPoint.html) | Get the location of a particular contact point in this contact pair.  
[GetSeparation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.GetSeparation.html) | Get the separation value at a particular contact point in this contact pair.  
[GetStaticFriction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.GetStaticFriction.html) | Get the static friction coefficient at a particular point of the contact pair.  
[GetTargetVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.GetTargetVelocity.html) | Get the target velocity the solver should aim reaching at a particular contact point in this contact pair.  
[IgnoreContact](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.IgnoreContact.html) | Ignore the specified contact point in this contact pair.  
[SetBounciness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.SetBounciness.html) | Set the restitution value for the specified contact point in this contact pair.  
[SetDynamicFriction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.SetDynamicFriction.html) | Set the value of the dynamic friction for a specified contact point in this contact pair.  
[SetMaxImpulse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.SetMaxImpulse.html) | Set the maximum impulse that the solver can apply at a particular contact point in this contact pair.  
[SetNormal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.SetNormal.html) | Set the normal at a particular contact point in this contact pair.  
[SetPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.SetPoint.html) | Set the location of a particular contact point in this contact pair.  
[SetSeparation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.SetSeparation.html) | Set the separation value at a particular contact point in this contact pair.  
[SetStaticFriction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.SetStaticFriction.html) | Set the static friction coefficient at a particular point of the contact pair.  
[SetTargetVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ModifiableContactPair.SetTargetVelocity.html) | Set the target velocity the solver should aim reaching at a particular contact point in this contact pair.  
* * *
