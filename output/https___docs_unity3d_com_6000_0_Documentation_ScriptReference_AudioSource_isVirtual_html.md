* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource-isVirtual.html

#  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).isVirtual
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
isVirtual; 
### Description
True if all sounds played by the AudioSource, such as main sound started by Play() or playOnAwake, and one-shots are culled by the audio system.
A sound is culled when its resulting volume is lower than the volumes of the N loudest voices, where N is the number of maximum audible sounds specified in the audio Project Settings or via [AudioConfiguration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioConfiguration.html).
* * *
