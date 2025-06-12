* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-maxDistance.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).maxDistance
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioSource.html "Go to AudioSource Component in the Manual")
maxDistance; 
### Description
The distance where sound either becomes inaudible or stops attenuation, depending on the rolloff mode.
[AudioRolloffMode.Linear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioRolloffMode.Linear.html): For the linear rolloff mode, the `maxDistance` is the point where the volume reaches zero and the sound becomes inaudible.   
  
[AudioRolloffMode.Custom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioRolloffMode.Custom.html): For the custom rolloff mode, the `maxDistance` sets the distance bounds of the curve. Any distance beyond holds the last available value.  
  
[AudioRolloffMode.Logarithmic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioRolloffMode.Logarithmic.html): For the logarithmic rolloff mode, the audio source ignores this setting. The sound will continue to attenuate with distance indefinitely. 
* * *
