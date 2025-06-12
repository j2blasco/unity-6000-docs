* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LimitVelocityOverLifetimeModule.html

# LimitVelocityOverLifetimeModule
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
Script interface for the Limit Velocity Over Lifetime module.
Additional resources: [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html), [ParticleSystem.limitVelocityOverLifetime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-limitVelocityOverLifetime.html).
### Properties
Property | Description  
---|---  
[dampen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LimitVelocityOverLifetimeModule-dampen.html) | Controls how much this module dampens particle velocities that exceed the velocity limit.  
[drag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LimitVelocityOverLifetimeModule-drag.html) | Controls the amount of drag that this modules applies to the particle velocities.  
[dragMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LimitVelocityOverLifetimeModule-dragMultiplier.html) | Specifies the drag multiplier.  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LimitVelocityOverLifetimeModule-enabled.html) | Specifies whether the LimitForceOverLifetimeModule is enabled or disabled.  
[limit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LimitVelocityOverLifetimeModule-limit.html) | Maximum velocity curve, when not using one curve per axis.  
[limitMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LimitVelocityOverLifetimeModule-limitMultiplier.html) | Change the limit multiplier.  
[limitX](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LimitVelocityOverLifetimeModule-limitX.html) | Maximum velocity curve for the x-axis.  
[limitXMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LimitVelocityOverLifetimeModule-limitXMultiplier.html) | Change the limit multiplier on the x-axis.  
[limitY](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LimitVelocityOverLifetimeModule-limitY.html) | Maximum velocity curve for the y-axis.  
[limitYMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LimitVelocityOverLifetimeModule-limitYMultiplier.html) | Change the limit multiplier on the y-axis.  
[limitZ](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LimitVelocityOverLifetimeModule-limitZ.html) | Maximum velocity curve for the z-axis.  
[limitZMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LimitVelocityOverLifetimeModule-limitZMultiplier.html) | Change the limit multiplier on the z-axis.  
[multiplyDragByParticleSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LimitVelocityOverLifetimeModule-multiplyDragByParticleSize.html) | Adjust the amount of drag this module applies to particles, based on their sizes.  
[multiplyDragByParticleVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LimitVelocityOverLifetimeModule-multiplyDragByParticleVelocity.html) | Adjust the amount of drag this module applies to particles, based on their speeds.  
[separateAxes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LimitVelocityOverLifetimeModule-separateAxes.html) | Set the velocity limit on each axis separately. This module uses ParticleSystem.LimitVelocityOverLifetimeModule.drag to dampen a particle's velocity if the velocity exceeds this value.  
[space](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LimitVelocityOverLifetimeModule-space.html) | Specifies if the velocity limits are in local space (rotated with the transform) or world space.  
* * *
