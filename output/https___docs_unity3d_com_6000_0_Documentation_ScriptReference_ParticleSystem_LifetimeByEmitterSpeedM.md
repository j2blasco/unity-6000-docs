* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LifetimeByEmitterSpeedModule.html

# LifetimeByEmitterSpeedModule
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
The Lifetime By Emitter Speed Module controls the initial lifetime of each particle based on the speed of the emitter when the particle was spawned.
This module multiplies the start lifetime of particles with a value that depends on the speed of the object that spawned them. For most Particle Systems, this is the GameObject velocity, but for sub-emitters, the velocity comes from the parent particle that the sub-emitter particle originated from.  
  
Additional resources: [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html), [ParticleSystem.MainModule.startLifetime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.MainModule-startLifetime.html).
### Properties
Property | Description  
---|---  
[curve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LifetimeByEmitterSpeedModule-curve.html) | Use this curve to define which value to multiply the start lifetime of a particle with, based on the speed of the emitter when the particle is spawned.  
[curveMultiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LifetimeByEmitterSpeedModule-curveMultiplier.html) | Use this property to change the curve multiplier.  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LifetimeByEmitterSpeedModule-enabled.html) | Use this property to enable or disable the LifetimeByEmitterSpeed module.  
[range](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.LifetimeByEmitterSpeedModule-range.html) | Control the start lifetime multiplier between these minimum and maximum speeds of the emitter.  
* * *
