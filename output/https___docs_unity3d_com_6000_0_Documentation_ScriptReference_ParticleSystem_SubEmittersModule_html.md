* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SubEmittersModule.html

# SubEmittersModule
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
Script interface for the SubEmittersModule.
The sub-emitters module allows you to spawn particles in child emitters from the positions of particles in the parent system.  
  
This module triggers child particle emission on events such as the birth, death, and collision of particles in the parent system.  
  
Additional resources: [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html), [ParticleSystem.subEmitters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-subEmitters.html).
### Properties
Property | Description  
---|---  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SubEmittersModule-enabled.html) | Specifies whether the SubEmittersModule is enabled or disabled.  
[subEmittersCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SubEmittersModule-subEmittersCount.html) | The total number of sub-emitters.  
### Public Methods
Method | Description  
---|---  
[AddSubEmitter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SubEmittersModule.AddSubEmitter.html) | Add a new sub-emitter.  
[GetSubEmitterEmitProbability](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SubEmittersModule.GetSubEmitterEmitProbability.html) | Gets the probability that the sub-emitter emits particles.  
[GetSubEmitterProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SubEmittersModule.GetSubEmitterProperties.html) | Gets the properties of the sub-emitter at the given index.  
[GetSubEmitterSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SubEmittersModule.GetSubEmitterSystem.html) | Gets the sub-emitter Particle System at the given index.  
[GetSubEmitterType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SubEmittersModule.GetSubEmitterType.html) | Gets the type of the sub-emitter at the given index.  
[RemoveSubEmitter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SubEmittersModule.RemoveSubEmitter.html) | Removes a sub-emitter from the given index in the array.  
[SetSubEmitterEmitProbability](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SubEmittersModule.SetSubEmitterEmitProbability.html) | Sets the probability that the sub-emitter emits particles.  
[SetSubEmitterProperties](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SubEmittersModule.SetSubEmitterProperties.html) | Sets the properties of the sub-emitter at the given index.  
[SetSubEmitterSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SubEmittersModule.SetSubEmitterSystem.html) | Sets the Particle System to use as the sub-emitter at the given index.  
[SetSubEmitterType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SubEmittersModule.SetSubEmitterType.html) | Sets the type of the sub-emitter at the given index.  
* * *
