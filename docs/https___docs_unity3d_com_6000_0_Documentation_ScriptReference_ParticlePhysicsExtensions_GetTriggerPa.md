* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticlePhysicsExtensions.GetTriggerParticles.html

#  [ParticlePhysicsExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticlePhysicsExtensions.html).GetTriggerParticles(ParticleSystem,ParticleSystemTriggerEventType,Particle[])
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
### Parameters
Parameter | Description  
---|---  
ps | Particle system.  
type | Type of trigger to return particles for.  
particles | The array of particles matching the trigger event type.  
### Returns
**void** Number of particles with this trigger event type. 
### Description
Get the particles that met the condition in the particle trigger module. Returns the number of particles written to the array.
This method is typically called from [MonoBehaviour.OnParticleTrigger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnParticleTrigger.html) in response to a trigger callback.
* * *
