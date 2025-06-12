* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCullingMode.html

# ParticleSystemCullingMode
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
The action to perform when the Particle System is offscreen.
### Properties
Property | Description  
---|---  
[Automatic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCullingMode.Automatic.html) | For looping effects, the simulation is paused when offscreen, and for one-shot effects, the simulation will continue playing.  
[PauseAndCatchup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCullingMode.PauseAndCatchup.html) | Pause the Particle System simulation when it is offscreen, and perform an extra simulation when the system comes back onscreen, creating the impression that it was never paused.  
[Pause](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCullingMode.Pause.html) | Pause the Particle System simulation when it is offscreen.  
[AlwaysSimulate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystemCullingMode.AlwaysSimulate.html) | Continue simulating the Particle System when it is offscreen.  
* * *
