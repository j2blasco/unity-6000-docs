* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.IsAlive.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).IsAlive
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
## Declaration
public bool IsAlive(); 
## Declaration
public bool IsAlive(bool withChildren = true); 
### Parameters
Parameter | Description  
---|---  
withChildren | Check all child Particle Systems as well.  
### Returns
**bool** True if the Particle System contains live particles or is still creating new particles. False if the Particle System has stopped emitting particles and all particles are dead. 
### Description
Does the Particle System contain any live particles, or will it produce more?
* * *
