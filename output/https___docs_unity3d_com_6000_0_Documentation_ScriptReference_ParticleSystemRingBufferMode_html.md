* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRingBufferMode.html

# ParticleSystemRingBufferMode
enumeration
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
Control how particles are removed from the Particle System.
### Properties
Property | Description  
---|---  
[Disabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRingBufferMode.Disabled.html) | Particles are removed when their age exceeds their lifetime.  
[PauseUntilReplaced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRingBufferMode.PauseUntilReplaced.html) | Particle ages pause at the end of their lifetime until they need to be removed. Particles are removed when creating new particles would exceed the Max Particles property.  
[LoopUntilReplaced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemRingBufferMode.LoopUntilReplaced.html) | Particle ages loop until they need to be removed. Particles are removed when creating new particles would exceed the Max Particles property.  
* * *
