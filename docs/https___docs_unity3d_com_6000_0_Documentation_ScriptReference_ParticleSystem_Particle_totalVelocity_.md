* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-totalVelocity.html

#  [ParticleSystem.Particle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html).totalVelocity
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) totalVelocity; 
### Description
The total velocity of the particle.
This is calculated as the sum of [ParticleSystem.Particle.velocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-velocity.html) and [ParticleSystem.Particle.animatedVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-animatedVelocity.html). Some particle features use the physics-based velocity, and other features use the animated velocity. Use this property to obtain the total combined velocity of the particle.
* * *
