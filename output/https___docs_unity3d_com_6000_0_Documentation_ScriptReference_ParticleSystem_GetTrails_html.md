* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.GetTrails.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).GetTrails
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
public [ParticleSystem.Trails](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Trails.html) GetTrails(); 
### Returns
**Trails** The variable to populate with the Trails that currently belong to the Particle System.. 
### Description
Returns all the data relating to the current internal state of the Particle System Trails.
If you want to restore the Particle System to its current state in the future, store the Trails this function returns along with [ParticleSystem.GetParticles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.GetParticles.html) and [ParticleSystem.GetPlaybackState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.GetPlaybackState.html).  
  
Additional resources: [Trails](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Trails.html), [SetTrails](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SetTrails.html), [GetPlaybackState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.GetPlaybackState.html).
* * *
## Declaration
public int GetTrails(ref [ParticleSystem.Trails](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Trails.html) trailData); 
### Parameters
Parameter | Description  
---|---  
trailData | The current Trails belonging to the Particle System.  
### Returns
**int** The number of trails. 
### Description
If you want to restore the Particle System to its current state in the future, store the Trails this function returns along with [ParticleSystem.GetParticles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.GetParticles.html) and [ParticleSystem.GetPlaybackState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.GetPlaybackState.html).  
  
This method allows you to get the trail data without creating any garbage, if you presize the trail data.  
  
Additional resources: [Trails](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Trails.html), [SetTrails](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SetTrails.html), [GetPlaybackState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.GetPlaybackState.html).
* * *
