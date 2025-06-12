* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-reverbZoneMix.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).reverbZoneMix
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
reverbZoneMix; 
### Description
The amount by which the signal from the AudioSource will be mixed into the global reverb associated with the Reverb Zones.
The range from 0 to 1 is linear (like the volume property) while the range from 1 to 1.1 is an extra boost range that allows you to boost the reverberated signal by 10 dB. The associated curve in combination with the distance-based attenuation curve is useful when trying to simulate transitions from near-field to distant sounds.  
  
Note that prior to Unity 5.0 reverb zones were not applied to 2D sounds. With the generalization of 2D and 3D sounds in Unity 5.0 through the Spatial Blend parameter the reverb can now be applied to any sound. Therefore when importing Unity projects made with versions prior to 5.0 this parameter will be set to 0 for all the sounds that were 2D sounds, but is now adjustable.
* * *
