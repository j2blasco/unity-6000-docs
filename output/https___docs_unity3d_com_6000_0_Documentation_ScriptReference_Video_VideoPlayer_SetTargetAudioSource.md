* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.SetTargetAudioSource.html

#  [VideoPlayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer.html).SetTargetAudioSource
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
## Declaration
public void SetTargetAudioSource(ushort trackIndex, [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) source); 
### Parameters
Parameter | Description  
---|---  
trackIndex | Index of the audio track to associate with the specified [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html).  
source |  [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) to associate with the audio track.  
### Description
Sets the [AudioSource](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AudioSource.html) that will receive audio samples for the specified track if this audio target is selected with [VideoPlayer.audioOutputMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-audioOutputMode.html).
* * *
