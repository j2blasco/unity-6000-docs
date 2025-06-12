* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html

# Particle
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
Script interface for a Particle.
Additional resources: [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html), [ParticleSystem.GetParticles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.GetParticles.html), [ParticleSystem.SetParticles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SetParticles.html).
### Properties
Property | Description  
---|---  
[angularVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-angularVelocity.html) | The angular velocity of the particle.  
[angularVelocity3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-angularVelocity3D.html) | The 3D angular velocity of the particle.  
[animatedVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-animatedVelocity.html) | The animated velocity of the particle.  
[axisOfRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-axisOfRotation.html) | Mesh particles rotate around this axis.  
[position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-position.html) | The position of the particle.  
[randomSeed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-randomSeed.html) | The random seed of the particle.  
[remainingLifetime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-remainingLifetime.html) | The remaining lifetime of the particle.  
[rotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-rotation.html) | The rotation of the particle.  
[rotation3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-rotation3D.html) | The 3D rotation of the particle.  
[startColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-startColor.html) | The initial color of the particle. The current color of the particle is calculated procedurally based on this value and the active color modules.  
[startLifetime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-startLifetime.html) | The starting lifetime of the particle.  
[startSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-startSize.html) | The initial size of the particle. The current size of the particle is calculated procedurally based on this value and the active size modules.  
[startSize3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-startSize3D.html) | The initial 3D size of the particle. The current size of the particle is calculated procedurally based on this value and the active size modules.  
[totalVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-totalVelocity.html) | The total velocity of the particle.  
[velocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-velocity.html) | The velocity of the particle, measured in units per second.  
### Public Methods
Method | Description  
---|---  
[GetCurrentColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.GetCurrentColor.html) | Calculate the current color of the particle by applying the relevant curves to its startColor property.  
[GetCurrentSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.GetCurrentSize.html) | Calculate the current size of the particle by applying the relevant curves to its startSize property.  
[GetCurrentSize3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.GetCurrentSize3D.html) | Calculate the current 3D size of the particle by applying the relevant curves to its startSize3D property.  
[GetMeshIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.GetMeshIndex.html) | Calculate the Mesh index of the particle, used for choosing which Mesh a particle is rendered with.  
[SetMeshIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.SetMeshIndex.html) | Sets the Mesh index of the particle, used for choosing which Mesh a particle is rendered with.  
* * *
