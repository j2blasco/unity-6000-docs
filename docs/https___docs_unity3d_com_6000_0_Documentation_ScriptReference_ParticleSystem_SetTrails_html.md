* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SetTrails.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).SetTrails
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
public void SetTrails([ParticleSystem.Trails](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.Trails.html) trailData); 
### Parameters
Parameter | Description  
---|---  
Trails | The Trails to apply to the Particle System.  
### Description
Use this method with the results of an earlier call to [ParticleSystem.GetTrails](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.GetTrails.html), in order to restore the Particle System to the state stored in the Trails object.
To fully restore a Particle System to a previous state, use this method along with [ParticleSystem.SetParticles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SetParticles.html) and [ParticleSystem.SetPlaybackState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SetPlaybackState.html).  
  
Additional resources: [GetTrails](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.GetTrails.html), [SetParticles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SetParticles.html), [SetPlaybackState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SetPlaybackState.html).
* * *
