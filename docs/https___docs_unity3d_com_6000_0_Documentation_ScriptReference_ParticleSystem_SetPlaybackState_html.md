* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SetPlaybackState.html

#  [ParticleSystem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.html).SetPlaybackState
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
public void SetPlaybackState([ParticleSystem.PlaybackState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.PlaybackState.html) playbackState); 
### Parameters
Parameter | Description  
---|---  
playbackState | The PlaybackState to apply to the Particle System.  
### Description
Use this method with the results of an earlier call to [ParticleSystem.GetPlaybackState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.GetPlaybackState.html), in order to restore the Particle System to the state stored in the playbackState object.
To fully restore a Particle System to a previous state, use this method along with [ParticleSystem.SetParticles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SetParticles.html) and [ParticleSystem.SetTrails](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SetTrails.html).  
  
Additional resources: [GetPlaybackState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.GetPlaybackState.html), [SetParticles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SetParticles.html), [SetTrails](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ParticleSystem.SetTrails.html).
* * *
