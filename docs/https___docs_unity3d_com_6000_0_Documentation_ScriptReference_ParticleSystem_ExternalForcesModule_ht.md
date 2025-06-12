* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.ExternalForcesModule.html

# ExternalForcesModule
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
Script interface for the ExternalForcesModule of a Particle System.
Additional resources: [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html), [ParticleSystem.externalForces](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem-externalForces.html).
### Properties
Property | Description  
---|---  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.ExternalForcesModule-enabled.html) | Specifies whether the ExternalForcesModule is enabled or disabled.  
[influenceCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.ExternalForcesModule-influenceCount.html) | The number of Force Fields explicitly provided to the influencers list.  
[influenceFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.ExternalForcesModule-influenceFilter.html) | Apply all Force Fields belonging to a matching Layer to this Particle System.  
[influenceMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.ExternalForcesModule-influenceMask.html) | Particle System Force Field Components with a matching Layer affect this Particle System.  
[multiplier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.ExternalForcesModule-multiplier.html) | Multiplies the magnitude of external forces affecting the particles.  
[multiplierCurve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.ExternalForcesModule-multiplierCurve.html) | Multiplies the magnitude of applied external forces.  
### Public Methods
Method | Description  
---|---  
[AddInfluence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.ExternalForcesModule.AddInfluence.html) | Adds a ParticleSystemForceField to the influencers list.  
[GetInfluence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.ExternalForcesModule.GetInfluence.html) | Gets the ParticleSystemForceField at the given index in the influencers list.  
[IsAffectedBy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.ExternalForcesModule.IsAffectedBy.html) | Determines whether any particles are inside the influence of a Force Field.  
[RemoveAllInfluences](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.ExternalForcesModule.RemoveAllInfluences.html) | Removes every Force Field from the influencers list.  
[RemoveInfluence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.ExternalForcesModule.RemoveInfluence.html) | Removes the Force Field from the influencers list at the given index.  
[SetInfluence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.ExternalForcesModule.SetInfluence.html) | Assigns the Force Field at the given index in the influencers list.  
* * *
