* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-spatialBlend.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).spatialBlend
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
spatialBlend; 
### Description
Sets how much this AudioSource is affected by 3D spatialisation calculations (attenuation, doppler etc). 0.0 makes the sound full 2D, 1.0 makes it full 3D.
Aside from determining if this AudioSource is heard as a 2D or 3D source, this property is useful to morph between the two modes.  
  
3D spatial calculations are applied after stereo panning is determined and can be used in conjunction with panStereo.  
  
Morphing between the 2 modes is useful for sounds that should be progressively heard as normal 2D sounds the closer they are to the listener.
* * *
