* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-velocity.html

#  [ParticleSystem.Particle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html).velocity
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) velocity; 
### Description
The velocity of the particle, measured in units per second.
This velocity is used for effects that are based on physics. Examples of features that use this type of velocity are the Force module, Gravity, and Start Speed. The system stores this velocity across frames, and reapplies it to the particle position on each simulation step.  
  
The velocity is also used by the [ParticleSystemRenderer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderer.html) if _Render Mode_ is set to [ParticleSystemRenderMode.Stretch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRenderMode.Stretch.html).  
  
Additional resources: [ParticleSystem.Particle.animatedVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-animatedVelocity.html), [ParticleSystem.Particle.totalVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-totalVelocity.html).
* * *
