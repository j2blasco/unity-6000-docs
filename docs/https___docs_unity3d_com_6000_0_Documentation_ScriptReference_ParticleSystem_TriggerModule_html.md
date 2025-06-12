* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TriggerModule.html

# TriggerModule
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
Script interface for the TriggerModule.
This module is useful for killing particles when they touch a set of collision shapes, or for calling a script command to let you apply custom particle behaviors when the trigger is activated.  
  
The example code for [MonoBehaviour.OnParticleTrigger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnParticleTrigger.html) shows how the callback type action works.  
  
Additional resources: [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html), [ParticleSystem.trigger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-trigger.html).
### Properties
Property | Description  
---|---  
[colliderCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TriggerModule-colliderCount.html) | Indicates the number of collision shapes attached to this Particle System trigger.  
[colliderQueryMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TriggerModule-colliderQueryMode.html) | Determines whether collider information is available when calling [[ParticleSystem::GetTriggerParticles]].  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TriggerModule-enabled.html) | Specifies whether the TriggerModule is enabled or disabled.  
[enter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TriggerModule-enter.html) | Choose what action to perform when particles enter the trigger volume.  
[exit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TriggerModule-exit.html) | Choose what action to perform when particles leave the trigger volume.  
[inside](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TriggerModule-inside.html) | Choose what action to perform when particles are inside the trigger volume.  
[outside](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TriggerModule-outside.html) | Choose what action to perform when particles are outside the trigger volume.  
[radiusScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TriggerModule-radiusScale.html) | A multiplier Unity applies to the size of each particle before it processes overlaps.  
### Public Methods
Method | Description  
---|---  
[AddCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TriggerModule.AddCollider.html) | Adds a Collision shape associated with this Particle System trigger.  
[GetCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TriggerModule.GetCollider.html) | Gets a collision shape associated with this Particle System trigger.  
[RemoveCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TriggerModule.RemoveCollider.html) | Removes a collision shape associated with this Particle System trigger.  
[SetCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.TriggerModule.SetCollider.html) | Sets a Collision shape associated with this Particle System trigger.  
* * *
