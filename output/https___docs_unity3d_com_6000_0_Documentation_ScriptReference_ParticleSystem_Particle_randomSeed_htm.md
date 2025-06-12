* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle-randomSeed.html

#  [ParticleSystem.Particle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Particle.html).randomSeed
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
randomSeed; 
### Description
The random seed of the particle.
Each particle has its own seed, in order to produce deterministic results during simulation. For example, if a particle uses a random color selected from a gradient, the seed ensures that the same color is generated on each frame.  
  
You may also use this seed when generating per-particle random numbers, by passing it to [Random.InitState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.InitState.html).
* * *
