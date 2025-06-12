* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule.html

# CollisionModule
struct in UnityEngine
/
Implemented in:[UnityEngine.ParticleSystemModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.ParticleSystemModule.html)
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html "Go to ParticleSystem Component in the Manual")
### Description
Script interface for the CollisionModule of a Particle System.
Additional resources: [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html), [ParticleSystem.collision](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-collision.html).
### Properties
Property | Description  
---|---  
[bounce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-bounce.html) | How much force is applied to each particle after a collision.  
[bounceMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-bounceMultiplier.html) | A multiplier for ParticleSystem.CollisionModule.bounce.  
[colliderForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-colliderForce.html) | How much force is applied to a Collider when hit by particles from this Particle System.  
[collidesWith](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-collidesWith.html) | Control which Layers this Particle System collides with.  
[dampen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-dampen.html) | How much speed does each particle lose after a collision.  
[dampenMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-dampenMultiplier.html) | Change the dampen multiplier.  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-enabled.html) | Specifies whether the CollisionModule is enabled or disabled.  
[enableDynamicColliders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-enableDynamicColliders.html) | Allow particles to collide with dynamic colliders when using world collision mode.  
[lifetimeLoss](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-lifetimeLoss.html) | How much a collision reduces a particle's lifetime.  
[lifetimeLossMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-lifetimeLossMultiplier.html) | Change the lifetime loss multiplier.  
[maxCollisionShapes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-maxCollisionShapes.html) | The maximum number of collision shapes Unity considers for particle collisions. It ignores excess shapes. Terrains take priority.  
[maxKillSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-maxKillSpeed.html) | Kill particles whose speed goes above this threshold, after a collision.  
[minKillSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-minKillSpeed.html) | Kill particles whose speed falls below this threshold, after a collision.  
[mode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-mode.html) | Choose between 2D and 3D world collisions.  
[multiplyColliderForceByCollisionAngle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-multiplyColliderForceByCollisionAngle.html) | Specifies whether the physics system considers the collision angle when it applies forces from particles to Colliders.  
[multiplyColliderForceByParticleSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-multiplyColliderForceByParticleSize.html) | Specifies whether the physics system considers particle sizes when it applies forces to Colliders.  
[multiplyColliderForceByParticleSpeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-multiplyColliderForceByParticleSpeed.html) | Specifies whether the physics system considers particle speeds when it applies forces to Colliders.  
[planeCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-planeCount.html) | Shows the number of planes currently set as Colliders.  
[quality](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-quality.html) | Specifies the accuracy of particle collisions against colliders in the Scene.  
[radiusScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-radiusScale.html) | A multiplier that Unity applies to the size of each particle before collisions are processed.  
[sendCollisionMessages](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-sendCollisionMessages.html) | Send collision callback messages.  
[type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-type.html) | The type of particle collision to perform.  
[voxelSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule-voxelSize.html) | Size of voxels in the collision cache.  
### Public Methods
Method | Description  
---|---  
[AddPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule.AddPlane.html) | Adds a collision plane to use with this Particle System.  
[GetPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule.GetPlane.html) | Get a collision plane associated with this Particle System.  
[RemovePlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule.RemovePlane.html) | Removes a collision plane associated with this Particle System.  
[SetPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.CollisionModule.SetPlane.html) | Set a collision plane to use with this Particle System.  
* * *
